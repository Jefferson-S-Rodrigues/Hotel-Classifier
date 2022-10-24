import os
import pymongo

user = os.environ.get('MONGO_USERNAME')
password = os.environ.get('MONGO_PASSWORD')
host = 'mongo'
port = '27017'

myclient = pymongo.MongoClient(f"mongodb://{user}:{password}@{host}:{port}/")

mydb = myclient["mlphotel"]

mycol = mydb["logclass"]


def register_use(request):
    mycol.insert_one(request)
