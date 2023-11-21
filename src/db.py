from typing import Dict
from bson import ObjectId
import pymongo
from src.utils import config

client = pymongo.MongoClient(config['db']['mongo']['uri'])


def insert_user(user: Dict):
    db = client[config['db']['mongo']['db']]
    collection = db['user']
    inserted_id = collection.insert_one(user)
    print(f"insert user with id: {inserted_id} successful")
    
    
def get_user(user: Dict):
    db = client[config['db']['mongo']['db']]
    collection = db['user']
    user = collection.find_one({
        'username': user['username'],
        'password': user['password']
    })
    return user

def get_user_by_id(user_id: str):
    db = client[config['db']['mongo']['db']]
    collection = db['user']
    user = collection.find_one({
        '_id': ObjectId(user_id)
    })
    return user
