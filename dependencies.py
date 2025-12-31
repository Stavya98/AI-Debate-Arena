"""from fastapi import Header, HTTPException
from auth import verify_user

def get_current_user(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Not authenticated")

    token = authorization.replace("Bearer ", "")
    try:
        return verify_user(token)
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")
"""

from fastapi import Cookie, HTTPException
from auth import verify_user

def get_current_user(auth_token: str = Cookie(None)):
    if not auth_token:
        raise HTTPException(status_code=401, detail="Not authenticated")

    try:
        return verify_user(auth_token)
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")
