from datetime import datetime
from .models import normalize_data
from pymongo import MongoClient
import pandas as pd

def insert_data(records, db):
    collection = db['courses']
    collection.create_index("createdAt", expireAfterSeconds=600)
    for record in records:
        record['createdAt'] = datetime.utcnow()
    collection.insert_many(records)

def check_and_refresh_data(url, db):
    collection = db['courses']
    if collection.count_documents({}) == 0:
        records = normalize_data(url)
        insert_data(records, db)
