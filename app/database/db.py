from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client.get_default_database()
applicants_collection = db["applicants"]
jobs_collection = db["jobs"]
categorization_collection = db["categorization"]