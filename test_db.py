import psycopg2

try:
    conn = psycopg2.connect(
        dbname="jobs_db",
        user="yogesh",
        password="1234",
        host="localhost",
        port="5432"
    )

    print("✅ Connected to PostgreSQL")

    conn.close()

except Exception as e:
    print("❌ Error:", e)