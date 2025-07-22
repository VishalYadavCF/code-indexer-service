import os
from db_clients.mongo_client import db

def test_mongo_client():
    try:
        # Try listing collection names
        collections = db.list_collection_names()
        print(f"MongoDB client is working. Collections: {collections}")
        return True
    except Exception as e:
        print(f"MongoDB client test failed: {e}")
        return False

if __name__ == "__main__":
    test_mongo_client()

