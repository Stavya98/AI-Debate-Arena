import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)

db = client['ai_debate_arena']

users_col = db['users']
debates_col = db['debates']