from pymongo import MongoClient
from pymongo import InsertOne
import yaml

class MongoDBInserter:
    client = MongoClient("localhost", 27017)
    db = client["vdb"]
    collection = db["md_accidents"]

    def __init__(self) -> None:
        pass

    def insert_data(self, data):
        self.collection.insert_one(data)
    
    def drop_collection(self):
        self.collection.drop()