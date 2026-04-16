import psycopg2

def load_data(data):
    conn = psycopg2.connect(
        dbname="jobs_db",
        user="yogesh",
        password="1234",
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()

    insert_query = """
        INSERT INTO jobs (title, company, location, salary)
        VALUES (%s, %s, %s, %s)
    """

    records = []
    for job in data:
        records.append((
            job.get("title"),
            job.get("company"),
            job.get("location"),
            job.get("salary")
        ))

    cur.executemany(insert_query, records)

    conn.commit()
    cur.close()
    conn.close()

    print(f" Inserted {len(records)} rows")