from config.database import conn, meta, engine
from sqlalchemy import Column, Integer, String, ForeignKey, Text, Boolean, Table

users = Table ('users', meta, 
    Column('id', Integer, primary_key = True),
    Column('username',String(40), unique = False, nullable = True),
    Column('email', String(40), unique = False, nullable = True),
    Column('password', String(256), nullable = False),
    Column('job_title', String(30), nullable = False)
)

# position_m = Table('position', meta,
#     Column('position_id', Integer, primary_key= True, autoincrement= True),
#     Column('position_name', String(100))    
# )

meta.create_all(engine)

