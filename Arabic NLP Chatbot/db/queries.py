import sqlite3

DB_PATH = "db/business.db"

def get_product(name):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT name, price, sizes, colors FROM products WHERE name = ?",
        (name,)
    )

    row = cursor.fetchone()
    conn.close()

    if not row:
        return None

    return {
        "name": row[0],
        "price": row[1],
        "sizes": row[2],
        "colors": row[3]
    }
