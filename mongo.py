from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

def save_links(base, data, db_name='crawler', collection_name='urls')
    db = client[db_name]
    collection = db[collection_name]
    document = collection.update(
        {'base': base},
        {'$set': data},
        True
    )
    return document