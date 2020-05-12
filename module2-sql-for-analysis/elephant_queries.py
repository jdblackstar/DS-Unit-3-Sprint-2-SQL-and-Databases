import psycopg2 as psycho

DB_NAME="ixcugnqx"
DB_USER="ixcugnqx"
DB_PW="7G_ii_FI2UJZIsFuhIzy7eA0eUB6Eylp"
DB_HOST="hansken.db.elephantsql.com"

conn = psycho.connect(dbname=DB_NAME, user=DB_USER, password=DB_PW, host=DB_HOST)
print(type(connection))

cursor = connection.cursor()
print(type(cursor))

breakpoint()

cursor.execute("SELECT * from test_table;")

results = cursor.fetchone()