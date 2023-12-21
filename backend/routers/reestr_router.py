from fastapi import APIRouter
from config.database import conn
from models.users import users
from schemas.users import User


user_routers = APIRouter()


@user_routers.get('/')
async def fetch_all_users():
    return conn.execute(users.select()).fetchall()

@user_routers.post('/')
async def create_users(user: User):
    conn.execute(users.insert().values(username = user.username, 
                                       email = user.email, 
                                       password = user.password, 
                                       job_title = user.job_title)
                )
    return conn.execute(users.select()).fetchall()

@user_routers.put('/{id}')
async def update_users(user: User, id: int):
    conn.execute(users.update().values(username = user.username, 
                                       email = user.email, 
                                       password = user.password, 
                                       job_title = user.job_title).where(users.c.id == id)
                )
    return conn.execute(users.select().where(users.c.id == id)).first()

@user_routers.delete('/{id}')
async def delete_users(user: User, id: int):
    conn.execute(users.delete().where(users.c.id == id))
    return conn.execute(users.select().where(users.c.id == id)).first()
