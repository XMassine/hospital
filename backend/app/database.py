from pymongo import MongoClient
from neo4j import GraphDatabase
import os

mongo_client = MongoClient("mongodb://mongo:27017")
mongodb = mongo_client["cabinet_db"]

neo4j_driver = GraphDatabase.driver("bolt://neo4j:7687", auth=("neo4j", "test"))
