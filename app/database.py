import sqlite3
from app.queries import Queries
from app.config import DB_FILE

def get_db_connection():
    return sqlite3.connect(DB_FILE)

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(Queries.CREATE_ORDERS_TABLE)
    conn.commit()
    conn.close()
