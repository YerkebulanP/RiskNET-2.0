from fastapi import FastAPI, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session

from config.database import engine
from routers.users_router import user_routers
from routers.reestr_router import reestr_routers

tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "reestr",
        "description": "Manage reestr."
    },
]

app = FastAPI(openapi_tags=tags_metadata)


app.include_router(user_routers)
app.include_router(reestr_routers)
