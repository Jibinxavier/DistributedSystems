from common.utils import UserDb,standup_db
from pymongo import MongoClient 

def build_test_db(host="localhost",port=27017, collection_name="test-collection"):
    standup_db()

    client = MongoClient(host,port)
    db = client['user-db']
    collection = db[collection_name]
    return collection
 

