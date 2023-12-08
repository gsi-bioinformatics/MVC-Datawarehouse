from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

load_dotenv()
def get_db():
    #Initialize Mongodb
    username=os.getenv('USER_MONGO')
    password=os.getenv('PASS_MONGO')
    uri = f"mongodb+srv://{username}:{password}@nosql-instance-01.k08ryrh.mongodb.net/?retryWrites=true&w=majority"

    #Access Catalog Collection

    client = MongoClient(uri,server_api=ServerApi('1'))
    db = client['BDO']
    catalog_collection = db["CatalogEntry"]
    return db