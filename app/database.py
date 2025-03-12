from pymongo import MongoClient
import os
from datetime import datetime

# MongoDB Connection URI (Default for local setup)
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

client = MongoClient(MONGO_URI)
db = client["execution_db"]
collection = db["executions"]

def store_execution_result(execution_id, code, output):
    """Stores execution results in MongoDB."""
    execution_data = {
        "execution_id": execution_id,
        "code": code,
        "output": output,
        "timestamp": datetime.utcnow(),
    }
    collection.insert_one(execution_data)

def get_execution_result(execution_id):
    """Retrieves execution results by ID from MongoDB."""
    result = collection.find_one({"execution_id": execution_id}, {"_id": 0})
    return result
