from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

def save_links(db_name, collection_name, data)
    db = client[db_name]
    collection = db[collection_name]
    document = collection.insert_one(data)
    return document