from pymongo import MongoClient

def get_db():
    client = MongoClient('localhost:27017')
    db = client.myFirstMB
    return db