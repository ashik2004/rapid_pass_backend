# The function of this file is to check whether the request is authorized or not [ verification of the protected route ]

from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .jwt_handler import decodeJWT


class jwtBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(jwtBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(jwtBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail="Invalid or Expired token!")
            return credentials.credentials
        else:
            raise HTTPException(
                status_code=403, detail="Invalid or Expired token!")


def verify_jwt(jwt_token: str):
    if jwt_token:
        try:
            payload = decodeJWT(jwt_token)
        except:
            pass
        if payload:
            return True
    return False
