from flask import Flask, render_template, request, redirect, session
from db import get_connection
from flask import jsonify

app = Flask(__name__)
app.secret_key = "youtubeanalytics2026"


# -------------------- LOGIN --------------------

@app.route("/")
def login_page():

    if "user" in session:
        return render_template("index.html")

    return render_template("login.html")


# -------------------- SIGNUP PAGE --------------------

@app.route("/signup")
def signup_page():

    return render_template("signup.html")


# -------------------- CREATE ACCOUNT --------------------

@app.route("/signup", methods=["POST"])
def signup():

    fullname = request.form["fullname"]
    email = request.form["email"]
    password = request.form["password"]
    confirm = request.form["confirm"]

    if password != confirm:
        return render_template(
        "signup.html",
        error="Passwords do not match."
    )

    conn = get_connection()

    if conn is None:
        return "Database Connection Failed"

    cursor = conn.cursor()

    # Check if email already exists

    cursor.execute(
        """
        SELECT * FROM users
        WHERE email=%s
        """,
        (email,)
    )

    existing = cursor.fetchone()

    if existing:

        cursor.close()
        conn.close()

        return render_template(
        "signup.html",
        error="An account with this email already exists."
    )

    cursor.execute(
        """
        INSERT INTO users(fullname,email,password)
        VALUES(%s,%s,%s)
        """,
        (fullname, email, password)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return redirect("/")


# -------------------- LOGIN CHECK --------------------

@app.route("/login", methods=["POST"])
def login():

    email = request.form["email"]
    password = request.form["password"]

    conn = get_connection()

    if conn is None:
        return "Database Connection Failed"

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT fullname
        FROM users
        WHERE email=%s
        AND password=%s
        """,
        (email, password)
    )

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if user:

        session["user"] = user[0]

        return redirect("/home")

    return render_template(
        "login.html",
        error="Invalid email or password."
    )


# -------------------- LOGOUT --------------------

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")


# -------------------- HOME --------------------

@app.route("/home")
def home():

    if "user" not in session:
        return redirect("/")

    return render_template("index.html")


# -------------------- DASHBOARD --------------------

@app.route("/dashboard", methods=["POST"])
def dashboard():

    if "user" not in session:
        return redirect("/")

    channel_name = request.form["channel"]

    conn = get_connection()

    if conn is None:
        return "Database Connection Failed"

    cursor = conn.cursor()

    # Save Search History

    cursor.execute(
        """
        INSERT INTO search_history(channel_name)
        VALUES(%s)
        """,
        (channel_name,)
    )

    conn.commit()

    # Get Channel

    cursor.execute(
        """
        SELECT
            id,
            channel_name,
            subscribers,
            views,
            videos,
            country,
            description
        FROM channels
        WHERE LOWER(channel_name)=LOWER(%s)
        """,
        (channel_name,)
    )

    result = cursor.fetchone()

    if result is None:

        cursor.close()
        conn.close()

        return render_template(
            "dashboard.html",
            channel=None,
            videos=[],
            labels=[],
            subscriber_data=[],
            view_data=[]
        )

    channel = {

        "id": result[0],
        "channel_name": result[1],
        "subscribers": result[2],
        "views": result[3],
        "videos": result[4],
        "country": result[5],
        "description": result[6]

    }

    # Recent Videos

    cursor.execute(
        """
        SELECT
            title,
            views,
            likes
        FROM videos
        WHERE channel_id=%s
        ORDER BY upload_date DESC
        LIMIT 5
        """,
        (channel["id"],)
    )

    videos = cursor.fetchall()

    # Analytics

    cursor.execute(
        """
        SELECT
            recorded_date,
            subscribers,
            views
        FROM analytics
        WHERE channel_id=%s
        ORDER BY recorded_date
        """,
        (channel["id"],)
    )

    analytics = cursor.fetchall()

    labels = []
    subscriber_data = []
    view_data = []

    for row in analytics:

        labels.append(row[0].strftime("%b %Y"))
        subscriber_data.append(row[1])
        view_data.append(row[2])

    cursor.close()
    conn.close()

    return render_template(
        "dashboard.html",
        channel=channel,
        videos=videos,
        labels=labels,
        subscriber_data=subscriber_data,
        view_data=view_data
    )


# -------------------- HISTORY --------------------

@app.route("/history")
def history():

    if "user" not in session:
        return redirect("/")

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT channel_name, searched_at
        FROM search_history
        ORDER BY searched_at DESC
        """
    )

    history = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        "history.html",
        history=history
    )


@app.route("/suggest")
def suggest():

    query = request.args.get("q", "").strip()

    conn = get_connection()
    cursor = conn.cursor()

    if query == "":
        cursor.execute("""
            SELECT DISTINCT channel_name
            FROM search_history
            ORDER BY searched_at DESC
            LIMIT 5
        """)
    else:
        cursor.execute("""
            SELECT channel_name
            FROM channels
            WHERE LOWER(channel_name)
            LIKE LOWER(%s)
            LIMIT 5
        """, (query + "%",))

    results = [row[0] for row in cursor.fetchall()]

    cursor.close()
    conn.close()

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)