# from fastapi import APIRouter
# from config.database import conn
# from models.users import users
# from schemas.schemas import User


# user_routers = APIRouter()


# @user_routers.get('/', tags=["users"])
# async def fetch_all_users():
#     return conn.execute(users.select()).fetchall()

# @user_routers.post('/', tags=["users"])
# async def create_users(user: User):
#     conn.execute(users.insert().values(username = user.username, 
#                                        email = user.email, 
#                                        password = user.password, 
#                                        job_title = user.job_title,
#                                     #    position_id = user.position_id
#                                        )
#                 )
#     return conn.execute(users.select()).fetchall()

# @user_routers.put('/{id}', tags=["users"])
# async def update_users(user: User, id: int):
#     conn.execute(users.update().values(username = user.username, 
#                                        email = user.email, 
#                                        password = user.password, 
#                                        job_title = user.job_title)
#                                     #    position_id = user.position_id)
#                                     .where(users.c.id == id)
#                 )
#     return conn.execute(users.select().where(users.c.id == id)).first()

# @user_routers.delete('/{id}', tags=["users"])
# async def delete_users(user: User, id: int):
#     conn.execute(users.delete().where(users.c.id == id))
#     return conn.execute(users.select().where(users.c.id == id)).first()

from fastapi import APIRouter
from config.database import conn
from models.users import Users, Positions
from schemas.schemas import User, Position, UserCreate
from sqlalchemy import select, join

user_routers = APIRouter()

@user_routers.get('/', tags=["users"])
async def fetch_all_users():
    query = (select(
                Users.username,
                Users.email,
                Users.password,
                Users.job_title,
                Positions.position_name).select_from(join(Users, Positions, Users.position_id == Positions.position_id))
    )   
    result = conn.execute(query).fetchall()
    return result

@user_routers.post('/', tags=["users"])
async def create_users(user: User):
    conn.execute(Users.__table__.insert().values(username=user.username, 
                                        email=user.email, 
                                        password=user.password, 
                                        job_title=user.job_title,
                                        position_id=user.position.position_id)
                )
    return conn.execute(select(Users)).fetchall()

@user_routers.put('/{id}', tags=["users"])
async def update_users(user: User, id: int):
    conn.execute(Users.__table__.update().values(username=user.username, 
                                        email=user.email, 
                                        password=user.password, 
                                        job_title=user.job_title,
                                        position_id=user.position.position_id)
                .where(Users.id == id)
                )
    return conn.execute(select(Users).where(Users.id == id)).first()


@user_routers.delete('/{id}', tags=["users"])
async def delete_users(id: int):
    conn.execute(delete(Users).where(Users.id == id))

    return conn.execute(select(Users).where(Users.id == id)).first()
