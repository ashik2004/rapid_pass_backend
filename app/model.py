from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    name: str = Field(min_length=1, max_length=50, default=None)
    email: EmailStr = Field(default=None)
    password: str = Field(min_length=6, max_length=50, default=None)
    class Config:
        the_schema = {
            "name": "Rahi Jamil",
            "email": "cs.mohammadrahi@gmail.com",
            "password": "123456"
        }

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(default=None)
    password: str = Field(min_length=6, max_length=50, default=None)
    class Config:
        the_schema = {
            "email": "cs.mohammadrahi@gmail.com",
            "password": "123456"
        }
