from pymongo import MongoClient

uri = "mongodb+srv://admin:admin@container.qdz4bit.mongodb.net/?retryWrites=true&w=majority"

conn = MongoClient(uri)

db = conn.snakeAndLadders