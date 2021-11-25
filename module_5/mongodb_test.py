from pymongo import MongoClient

"""
URL for MongoDB connection
"""

url = "mongodb+srv://admin:admin@cluster0.qghgj.mongodb.net/Cluster0?retryWrites=true&w=majority"

"""
Client for Mongo using URL above
"""

client = MongoClient(url)

"""
DB Variable for pytech
"""
db = client.pytech

print(db.list_collection_names)
