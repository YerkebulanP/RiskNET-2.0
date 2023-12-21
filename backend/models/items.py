from sqlalchemy import create_engine, Column, Integer, String, Float
from pydantic import BaseModel
from sqlalchemy.orm import sessionmaker




# class ItemBase(BaseModel):
#     __tablename__ = 'items'

#     name: str
#     calories: float
#     fat: float
#     carbs: float
#     protein: float

# class ItemCreate(ItemBase):
#     pass

# class Item(ItemBase):
#     id: int

#     class Config:
#         orm_mode = True


