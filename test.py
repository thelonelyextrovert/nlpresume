import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://surya_mongodb:P3ass57word@cluster0.6ns8n.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = cluster["resume"]
collection = db["resume"]

results = collection.remove({})