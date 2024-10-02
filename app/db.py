from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

client = None
db = None

async def connect_to_mongo():
    global client
    client = AsyncIOMotorClient(settings.MONGODB_URL)
    global db
    db = client[settings.MONGODB_DB_NAME]
    print("Connected to MongoDB")

async def close_mongo_connection():
    global client
    if client:
        client.close()
    print("MongoDB connection closed")

from pymongo import MongoClient

# MongoDB Connection (adjust this for your environment)
client = MongoClient('mongodb://localhost:27017')
db = client['customer_database']

def get_db():
    return db
