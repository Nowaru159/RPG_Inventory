import sqlite3

conn = sqlite3.connect('bdd/bdd_item.db')
cursor = conn.cursor()

cursor.execute(
    "CREATE TABLE item ("
    "id INTEGER PRIMARY KEY AUTOINCREMENT,"
    "name TEXT,"
    "quantity INTEGER,"
    "weight FLOAT,"
    "rarity TEXT,"
    "type TEXT,"
    "item_class TEXT)"
)

conn.commit()
conn.close()
