import os

import pymongo
from dotenv import load_dotenv
from pymongo.collection import Collection
from pymongo.database import Database

load_dotenv()


def connect() -> Collection:
    mongo_user = os.getenv('MONGO_USER')
    mongo_pass = os.getenv('MONGO_PASS')
    client = pymongo.MongoClient(
        f"mongodb+srv://{mongo_user}:{mongo_pass}@cluster0.smsj2.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db: Database = client['myFirstDatabase']
    col: Collection = db['chats']
    return col
