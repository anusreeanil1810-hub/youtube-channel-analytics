from flask import Flask, render_template, request
from db import get_connection

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard", methods=["POST"])
def dashboard():

    channel_name = request.form["channel"]

    conn = get_connection()

    if conn is None:
        return "Database Connection Failed"

    cursor = conn.cursor()

    # Save search history
    cursor.execute(
        """
        INSERT INTO search_history(channel_name)
        VALUES(%s)
        """,
        (channel_name,)
    )

    conn.commit()

    # Get channel details
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

    # Get latest videos
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

    # Get analytics history
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


if __name__ == "__main__":
    app.run(debug=True)