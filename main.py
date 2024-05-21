from fastapi import FastAPI, HTTPException, Body, Depends
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from app.model import UserSchema, UserLoginSchema
from database import create_user, login_user, initialize_database
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import jwtBearer

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def on_startup():
    await initialize_database()


@app.get("/", dependencies=[Depends(jwtBearer())], tags=['root'])
async def root():
    return {"message": "Hello RapidPass"}

# User Sign Up [ Create a new User ]


@app.post("/user/signup", tags=['user'])
async def user_signup(user: UserSchema = Body(default=None)):

    try:
        response = await create_user(user.dict())
        if response:
            return signJWT(user.email)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(400, "Something went wrong / Bad request")


@app.post("/user/login", tags=['user'])
async def user_login(user: UserLoginSchema = Body(default=None)):

    try:
        response = await login_user(user.email, user.password)
        if response:
            return signJWT(user.email)
        else:
            raise HTTPException(400, "Invalid email or password")
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(400, "Something went wrong / Bad request")
