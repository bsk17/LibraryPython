from pymongo import MongoClient
from main import Library

client = MongoClient(port=27017)
db = client.Books

