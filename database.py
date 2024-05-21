from motor.motor_asyncio import AsyncIOMotorClient
from app.model import UserSchema
from fastapi import HTTPException

client = AsyncIOMotorClient("mongodb://localhost:27017")

database = client.RapidPass

collection = database.users


async def initialize_database():
    await collection.create_index("email", unique=True)


async def login_user(email: str, password: str):
    document = await collection.find_one({"email": email, "password": password})
    return document


async def create_user(user: UserSchema):
    try:
        result = await collection.insert_one(user)
        return result
    except Exception as e:
        if e.details and "duplicate key error" in e.details["errmsg"]:
            raise HTTPException(400, "Email already exists")
        raise e
