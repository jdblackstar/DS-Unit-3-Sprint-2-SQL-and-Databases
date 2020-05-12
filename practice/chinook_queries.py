import sqlite3

DATABASE_FILEPATH = "chinook.db"

connection = sqlite3.connect(DATABASE_FILEPATH)
print(type(connection))

cursor = connection.cursor
print(type(cursor))

breakpoint()

query = "SELECT COUNT(*) FROM armory_item;"
cursor.execute(query)

cursor.execute(query).fetchall()