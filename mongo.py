from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

def save_links(base_url, data, db_name='crawler', collection_name='urls')
    db = client[db_name]
    collection = db[collection_name]
    document = collection.update(
        {'base_url': base_url},
        {'$set': data},
        True
    )
    return document