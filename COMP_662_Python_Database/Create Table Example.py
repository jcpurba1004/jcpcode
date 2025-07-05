import sqlite3

connection = sqlite3.connect('my_database.db') # Replace 'my_database.db' with your desired database file name
cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)
"""
cursor.execute(create_table_query)

insert_query = """
INSERT INTO users (name, age)
VALUES (?, ?)
"""
data = [
    ('Alice', 30),
    ('Bob', 25),
    ('Charlie', 35),
]
cursor.executemany(insert_query, data)

connection.commit()

connection.close()