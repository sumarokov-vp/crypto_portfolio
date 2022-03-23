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

s = get_setting('bot')
print(s)