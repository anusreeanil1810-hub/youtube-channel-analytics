from db import get_connection

conn = get_connection()

if conn:
    print("✅ Connected to ShaktiDB Successfully!")
    conn.close()
else:
    print("❌ Connection Failed")