import sqlite3

def connection():
    conn: sqlite3.Connection = sqlite3.connect('main.db')

    return conn


async def create_table():
    query = f"""CREATE TABLE IF NOT EXISTS users (
        user_id BIGINT PRIMARY KEY,
        full_name VARCHAR(255) NOT NULL,
        username VARCHAR(255),
        language VARCHAR(5) DEFAULT 'uz'
    )"""

    with connection() as conn:
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()


async def get_user_or_create(user_id: int, full_name: str, username: str | None, language: str):
    get_user_query = f"""SELECT * FROM users WHERE user_id = {user_id}"""
    create_user_query = f"""INSERT INTO users VALUES (?, ?, ?, ?)""", (user_id, full_name, username, language)

    with connection() as conn:
        cur = conn.cursor()
        user = (cur.execute(get_user_query)).fetchone()

        if not user:
            cur.execute(*create_user_query)
            conn.commit()

        user = (cur.execute(get_user_query)).fetchone()

        return user


async def get_user(user_id: int):
    with connection() as conn:
        cur = conn.cursor()
        query = f"""SELECT * FROM users WHERE user_id = {user_id}"""
        user = (cur.execute(query)).fetchone()

        return user