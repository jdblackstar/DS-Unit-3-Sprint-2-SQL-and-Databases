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

#
# INSERT SOME DATA
#

my_dict = {"a": 1, "b": ["dog", "cat", 42], "c": "true"}

# sql = f"""
# INSERT INTO test_table (name, data) VALUES
# ("A row name", null),
# ("Another row, with JSON", "{"a": 1, "b": ["dog", "cat", 42], "c": true}"::JSONB);
# """

# insertion_query = f"INERT INTO test_table (name, data) VALUES (%s, %s)"
# cursor.execute(insertion_query,
#     ("A rowwww", "null")
# )
# cursor.execute(insertion_query,
#     ("Another row, with JSONNNN", json.dumps(my_dict))
# )

# h/t: https://stackoverflow.com/questions/8134602/psycopg2-insert-multiple-rows-with-one-query
insertion_query = f"INSERT INTO test_table (name, data) VALUES %s"
execute_values(cursor, insertion_query, [
  ('A rowwwww', 'null'),
  ('Another row, with JSONNNNN', json.dumps(my_dict)),
  ('Third row', "3")
]) # third param: data as a list of tuples!

connection.commit() # actually save the records / run the transaction to insert rows

cursor.close()
connection.close()