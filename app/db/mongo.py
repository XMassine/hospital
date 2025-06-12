from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["cabinet"]  # ← remplace par le nom exact de ta base MongoDB

