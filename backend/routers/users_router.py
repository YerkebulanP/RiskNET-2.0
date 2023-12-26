from fastapi import APIRouter, Depends, HTTPException, Form
from config.database import conn, get_db
from models.users import Users
from schemas.schemas import User, UserCreate

from sqlalchemy import select, join
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
# from config import settings
from datetime import datetime, timedelta
import secrets

user_routers = APIRouter()

@user_routers.get('/', tags=["users"])
async def fetch_all_users():
    query = (select(
                Users.username,
                Users.lastname,
                Users.email,
                Users.password,
                Users.position
             )
    )   
    result = conn.execute(query).fetchall()
    return result

@user_routers.post('/', tags=["users"])
async def create_users(user: UserCreate):
    conn.execute(Users.__table__.insert().values(username=user.username,
                                        lastname=user.lastname, 
                                        email=user.email, 
                                        password=user.password, 
                                        position=user.position)
                )
    return conn.execute(select(Users)).fetchall()

@user_routers.put('/{id}', tags=["users"])
async def update_users(user: User, id: int):
    conn.execute(Users.__table__.update().values(username=user.username, 
                                        lastname=user.lastname, 
                                        email=user.email, 
                                        password=user.password, 
                                        position=user.position)
                .where(Users.id == id)
                )
    return conn.execute(select(Users).where(Users.id == id)).first()


@user_routers.delete('/{id}', tags=["users"])
async def delete_users(id: int):
    conn.execute(delete(Users).where(Users.id == id))

    return conn.execute(select(Users).where(Users.id == id)).first()


# AUTHORIZATION 
def authenticate_user(db: Session, email: str, password: str):
    user = db.query(Users).filter(Users.email == email, Users.password == password).first()
    return user

@user_routers.post("/loginasd", response_model = dict, operation_id="login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # You can customize this part based on your needs
    return {"message": "Login successful"}

# AUTH
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(email: str, password:str):
    user = conn.execute(select(Users).where(Users.email == email)).first()
    if user and user["password"] == password:
        return user
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")

# Function to generate a simple random token
def generate_token():
    return secrets.token_urlsafe(32)


import logging

logging.basicConfig(level=logging.DEBUG)


# Login endpoint
@user_routers.post("/login")
async def login(email: str = Form(...), password: str = Form(...)):
    logging.debug(f"Received login request with email: {email} and password: {password}")
    
    user = await get_current_user(email, password)
    
    if user:
        # Generate a simple random token
        token = generate_token()
        return {"access_token": token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")
