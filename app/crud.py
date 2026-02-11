from .database import get_db_connection
from . import schemas
import psycopg2.extras

def get_item(conn, item_id: int):
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute("SELECT * FROM items WHERE id = %s", (item_id,))
        item = cur.fetchone()
        return item

def get_items(conn, skip: int = 0, limit: int = 100):
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute("SELECT * FROM items ORDER BY id LIMIT %s OFFSET %s", (limit, skip))
        items = cur.fetchall()
        return items

def create_item(conn, item: schemas.ItemCreate):
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute(
            "INSERT INTO items (name, description) VALUES (%s, %s) RETURNING *",
            (item.name, item.description),
        )
        new_item = cur.fetchone()
        conn.commit()
        return new_item