from fastapi import FastAPI, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session

from config.database import engine
from routers.users_router import user_routers


app = FastAPI()


app.include_router(user_routers)


# Base.metadata.create_all(bind = engine)

# # Dependency
# def get_db() -> Session:
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.post("/items/", response_model=Item)
# def create_item(items: ItemCreate, db: Session = Depends(get_db)):
#     db.add(items)
#     db.commit()
#     db.refresh(items)
#     return items

# @app.get("/items/", response_model=List[Item])
# def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#    return db.query(Item).offset(skip).limit(limit).all()    

# @app.post('/')
# async def post_model():
#     return {'message':"Hellow world"}

   