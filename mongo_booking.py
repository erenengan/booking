import pandas as pd
import pymongo as pm
from pymongo import MongoClient
import csv

client = MongoClient('mongodb://127.0.0.1:27017/')
db = client['booking']
collection = db['hotels']

collection.insert_many(df.to_dict("records"))

collection.aggregate([
    {"$group": {
        "_id":"$Name",
        "averagePrice": {
            "$avg": "$Price"
            }
    }
    },
    {"$match":{
        "$expr": {
            "$lte": {"$Price", "$averagePrice"}
        }   
     }}
])

