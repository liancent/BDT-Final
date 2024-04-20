from pymongo import MongoClient

class MongoDBInserter:
    def __init__(self) -> None:
        pass

    def insert_data(self):
        client = MongoClient("localhost", 27017)
        db = client["vdb"]
        collection = db.get_collection["md_accidents"]