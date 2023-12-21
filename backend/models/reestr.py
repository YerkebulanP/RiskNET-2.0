from sqlalchemy import create_engine, Column, Integer, String, Float
from pydantic import BaseModel
from sqlalchemy.orm import sessionmaker

class Reestr(Base):
    __tablename__ = 'reestr'
    reestr_id = Column(Integer, primary_key = True)
    risk_year = Column(Integer)
    risk_quarter = Column(Integer, ForeignKey('quarter.quarter_id'))
    # risk_category = Column(String(50), ForeignKey('risk_category.risk_category_id') , nullable = True)
    # risk_tolerancy = Column(String(100))

meta.create_all(engine)
