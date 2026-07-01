import psycopg2

def get_connection():
    try:
        connection = psycopg2.connect(
            host="localhost",
            port="5432",
            database="youtube_analytics",
            user="anusree",
            password="8590404746"   # Leave empty for now
        )
        return connection

    except Exception as e:
        print("Database Connection Error:", e)
        return None