# inclass/elephant_queries.py
import os
#import json
from dotenv import load_dotenv # python-dotenv
import psycopg2
from psycopg2.extras import execute_values
import pandas
import numpy as np
load_dotenv() #> loads contents of the .env file into the script's environment
psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)
#
# READ PASSENGER DATA FROM THE CSV FILE
#
#CSV_FILEPATH = "titanic.csv"
#CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "titanic.csv")
CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "module2-sql-for-analysis", "titanic.csv")
df = pandas.read_csv(CSV_FILEPATH)
print(df.dtypes)
print(df.head())
#
# CONNECT TO THE PG DATABASE
#
DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PW = os.getenv("DB_PW", default="OOPS")
DB_HOST = os.getenv("DB_HOST", default="OOPS")
connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PW, host=DB_HOST)
print(type(connection)) #> <class 'psycopg2.extensions.connection'>
cursor = connection.cursor()
print(type(cursor)) #> <class 'psycopg2.extensions.cursor'>
#
# CREATE A TABLE TO STORE THE PASSENGERS
#
table_creation_sql = """
DROP TABLE IF EXISTS passengers;
CREATE TABLE IF NOT EXISTS passengers (
    id  SERIAL PRIMARY KEY,
    "survived" int4, -- consider boolean here
    "pclass" int4,
    "name" text,
    "sex" text,
    "age" int4,
    "sib_spouse_count" int4,
    "parent_child_count" int4,
    "fare" float8
);
"""
cursor.execute(table_creation_sql)
#
# INSERT DATA INTO THE PASSENGERS TABLE
#
# how to convert dataframe to a list of tuples?
list_of_tuples = list(df.to_records(index=False))
insertion_query = f"INSERT INTO passengers (survived, pclass, name, sex, age, sib_spouse_count, parent_child_count, fare) VALUES %s"
execute_values(cursor, insertion_query, list_of_tuples) # third param: data as a list of tuples!
connection.commit() # actually save the records / run the transaction to insert rows
cursor.close()
connection.close()