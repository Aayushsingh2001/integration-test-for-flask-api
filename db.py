import sqlite3

def init_db():
    conn = sqlite3.connect('items.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS items (name TEXT)')
    conn.commit()
    conn.close()

def get_items():
    conn = sqlite3.connect('items.db')
    c = conn.cursor()
    c.execute('SELECT name FROM items')
    items = [row[0] for row in c.fetchall()]
    conn.close()
    return items

def add_item(name):
    conn = sqlite3.connect('items.db')
    c = conn.cursor()
    c.execute('INSERT INTO items VALUES (?)', (name,))
    conn.commit()
    conn.close()
