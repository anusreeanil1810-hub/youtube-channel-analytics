from flask import Flask, render_template, request
from db import get_connection

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/dashboard', methods=['POST'])
def dashboard():

    channel_name = request.form['channel']

    conn = get_connection()

    if conn is None:
        return "Database Connection Failed"

    cursor = conn.cursor()

    # Save search history
    cursor.execute("""
        INSERT INTO search_history(channel_name)
        VALUES(%s)
    """, (channel_name,))
    conn.commit()

    # Fetch channel
    cursor.execute("""
        SELECT id,
               channel_name,
               subscribers,
               views,
               videos,
               country,
               description
        FROM channels
        WHERE LOWER(channel_name)=LOWER(%s)
    """, (channel_name,))

    result = cursor.fetchone()

    if result is None:
        cursor.close()
        conn.close()
        return render_template(
            "dashboard.html",
            channel=None,
            videos=[]
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

    # Fetch videos
    cursor.execute("""
        SELECT title,
               views,
               likes
        FROM videos
        WHERE channel_id=%s
        ORDER BY upload_date DESC
    """, (channel["id"],))

    videos = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        "dashboard.html",
        channel=channel,
        videos=videos
    )


if __name__ == "__main__":
    app.run(debug=True)