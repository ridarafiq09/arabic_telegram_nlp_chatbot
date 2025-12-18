import sqlite3

DB_PATH = "db/business.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create products table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        price INTEGER,
        sizes TEXT,
        colors TEXT
    )
    """)

    # Insert products 
    products = [
    ("فستان", 25, "S,M,L,XL", "أحمر,أسود,أزرق"),
    ("حذاء", 40, "38,39,40,41,42,43,44", "أسود,أبيض"),
    ("جاكيت", 60, "M,L,XL", "بني,أسود"),
]

    cursor.executemany("""
    INSERT OR IGNORE INTO products (name, price, sizes, colors)
    VALUES (?, ?, ?, ?)
    """, products)


    conn.commit()
    conn.close()
    print("✅ Database initialized")

if __name__ == "__main__":
    init_db()
