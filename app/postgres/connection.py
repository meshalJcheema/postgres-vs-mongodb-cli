import psycopg2

def get_pg_connection():
    return psycopg2.connect(
        dbname="db_a1",
        user="emumba",          # IMPORTANT
        host="localhost",
        port=5432
    )

