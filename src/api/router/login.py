import os
import requests

from dotenv import load_dotenv

from fastapi.responses import RedirectResponse
from fastapi.routing import APIRouter
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends

import jwt

# NOTE: Need to connect with Database.
# FIXME: POC for Security.
# FIXME: POC Starlette.


load_dotenv()
# Parsing .ENV
OAUTH_PROVIDER=os.getenv("OAUTH2_PROVIDER")
CLIENT_ID=os.getenv("CLIENT_ID")
CLIENT_SECRET=os.getenv("CLIENT_SECRET_ID")
REDIRECT_URI="http://localhost:8000/login/auth/google"

# Set tags for login page
tags = ["Authenthication System"]
path_prefix = os.getenv("LOGIN_PATH", default="/login")

# Set API Router
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
router_login = APIRouter(
    tags=tags,
    prefix=path_prefix, 
)

# Redirect to google Oauth.
@router_login.get("/google")
async def login_google():
    return RedirectResponse(url=f"https://accounts.google.com/o/oauth2/auth?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope=openid%20profile%20email&access_type=offline")
    
    
# Get token from google redirect
@router_login.get("/auth/google")
async def auth_google(code: str):
    token_url = "https://accounts.google.com/o/oauth2/token"
    data = {
        "code": code,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "grant_type": "authorization_code",
    }
    response = requests.post(token_url, data=data)
    access_token = response.json().get("access_token")
    user_info = requests.get("https://www.googleapis.com/oauth2/v1/userinfo", headers={"Authorization": f"Bearer {access_token}"})
    
    return user_info.json()


# Token from FastAPI
@router_login.get("/token")
async def get_token(token: str = Depends(oauth2_scheme)):
    return jwt.decode(token, CLIENT_SECRET, algorithms=["HS256"])