import psycopg
from db_connection import connection_string

def get_setting(key):
    with psycopg.connect(connection_string) as con:
        with con.cursor() as cur:
            query = """
                SELECT value FROM settings WHERE key = %s
                """
            result = cur.execute(query,(key,))
            value = result.fetchone()[0]
    return value

def create_user(name, chat_id):
    with psycopg.connect(connection_string) as con:
        with con.cursor() as cur:
            query = """
                INSERT INTO users (name, telegram)
                VALUES (%s, %s)
                RETURNING id;
                """
            try:
                result = cur.execute(query,(name, chat_id))
                con.commit()
                id = result.fetchone()[0]
            except Exception as e:
                id = None
    return id