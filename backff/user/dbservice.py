import os

import pymongo

user = os.environ.get('MONGO_USERNAME')
password = os.environ.get('MONGO_PASSWORD')
host = 'mongo'
port = '27017'

myclient = pymongo.MongoClient(f"mongodb://{user}:{password}@{host}:{port}/")

mydb = myclient["mlphotel"]

mycol = mydb["hotelauth"]

def save_user(user):
    u = user.__dict__
    if len(get_by_username(u['username'])) == 0:
        x = mycol.insert_one(u)
        return x
    else:
        raise UserException("Usuário já existe")

def get_by_username(username):
    result = mycol.find_one({"username": username})
    return result

class UserException(Exception):
    pass