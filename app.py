from flask import Flask
import psycopg2

app = Flask(__name__)

# Connect to ShaktiDB
conn = psycopg2.connect(
    dbname="youtube_analytics",
    user="anusree",
    host="/tmp"
)
@app.route("/")
def home():
    cur = conn.cursor()

    cur.execute("""
        SELECT video_title, views
        FROM video
        JOIN analytics
        ON video.video_id = analytics.video_id
        ORDER BY views DESC;
    """)

    videos = cur.fetchall()

    cur.close()

    html = """
    <h1>YouTube Channel Analytics</h1>
    <table border="1" cellpadding="10">
        <tr>
            <th>Video</th>
            <th>Views</th>
        </tr>
    """

    for video in videos:
        html += f"<tr><td>{video[0]}</td><td>{video[1]}</td></tr>"

    html += "</table>"

    return html

if __name__ == "__main__":
    app.run(debug=True)