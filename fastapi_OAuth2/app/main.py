from fastapi import FastAPI, Depends, HTTPException
from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from typing import Annotated, Any
from fakedb import fake_db  # Importing a fake database for demonstration

# Defining constants for JWT
ALGORITHM: str = "HS256"
SECRET_KEY: str = "my secret key"

# Function to create an access token
def create_access_token(subject: str, expires_delta: timedelta) -> str:
    expire = datetime.utcnow() + expires_delta
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Initializing the FastAPI app
app = FastAPI()

# Defining OAuth2PasswordBearer dependency
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Creating login route
@app.post("/login")
def login_request(user_data: Annotated[Any, Depends(OAuth2PasswordRequestForm)]):
    # Verify if the user exists in the fake database
    user_in_db = fake_db.get(user_data.username)
    if user_in_db is None:
        raise HTTPException(status_code=401, detail="Incorrect Username")

    # Verify if the entered password matches the stored password
    if user_in_db["password"] != user_data.password:
        raise HTTPException(status_code=401, detail="Incorrect Password")

    # Set the token expiry time
    access_token_expiry_minutes = timedelta(minutes=15)

    # Generate the access token
    generated_token = create_access_token(
        subject=user_data.username,
        expires_delta=access_token_expiry_minutes
    )

    # Return the username and generated access token
    return {"username": user_data.username, "access_token": generated_token}

# Route to get all users from the fake database
@app.get("/all-user")
def get_all_users(token: Annotated[str, Depends(oauth2_scheme)]):
    return fake_db

# A special endpoint that requires token authentication (a use case for multiple microservices)
@app.get("/special-endpoint")
def special_endpoint(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"user details": "Authorized User", "token": token}

# Route to get a token for a given username
@app.get("/get-token")
def get_token(name: str):
    access_token_expiry_minutes = timedelta(minutes=15)

    generated_token = create_access_token(
        subject=name,
        expires_delta=access_token_expiry_minutes
    )

    return {"access_token": generated_token}

# Function to decode an access token
def decode_access_token(access_token: str):
    decoded_jwt = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
    return decoded_jwt

# Route to decode a given token
@app.get("/decoded-token")
def decoding_token(access_token: str):
    try:
        decoded_jwt = decode_access_token(access_token)
        return {"decoded_token": decoded_jwt}
    except JWTError:
        return {"error": "Invalid token"}

# Multi microservice architecture OAuth

# Step 1: Creating a wrapper endpoint that will call the login endpoint and return the access token

# Step 2: Importing OAuth2PasswordBearer - token 
