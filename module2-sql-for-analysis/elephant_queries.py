import psycopg2 as psycho

DB_NAME="ixcugnqx"
DB_USER="ixcugnqx"
DB_PW="7G_ii_FI2UJZIsFuhIzy7eA0eUB6Eylp"
DB_HOST="hansken.db.elephantsql.com"

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PW, host=DB_HOST)
print(type(connection)) #> <class 'psycopg2.extensions.connection'>

cursor = connection.cursor()
print(type(cursor)) #> <class 'psycopg2.extensions.cursor'>

cursor.execute("SELECT * from test_table;") #TODO: share links related to this two step process

#results = cursor.fetchone()
results = cursor.fetchall()
for row in results:
    print(type(row), row)