import psycopg2

def get_connection():
    try:
        connection = psycopg2.connect(
            host="/tmp",
            port="5432",
            database="youtube_project",
            user="anusree",
            password="8590404746"
        )
        return connection

    except Exception as e:
        print("Database Connection Error:", e)
        return None