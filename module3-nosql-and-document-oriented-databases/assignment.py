# app/mongo_queries.py
import sqlite3
import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

# READ RPG DATA

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"

print("----------------")
print("URI:", connection_uri)

client = pymongo.MongoClient(connection_uri)

print("----------------")
print("CLIENT:", type(client), client)

#print(dir(client))
print("DB NAMES:", client.list_database_names()) #> ['admin', 'local']

db = client.ds14_db # "ds14_db" or whatever you want to call it
print("----------------")
print("DB:", type(db), db)

collection = db.ds14_pokemon_collection # "ds14_collection" or whatever you want to call it
print("----------------")
print("COLLECTION:", type(collection), collection)
print("----------------")
print("COLLECTIONS:")
print(db.list_collection_names())