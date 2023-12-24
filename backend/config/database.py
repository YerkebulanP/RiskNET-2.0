from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine(
        "postgresql://postgres:erkebulan2001@localhost:5432/asdasd", 
        echo = True
)

meta = MetaData()
conn = engine.connect()


# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:erkebulan2001@localhost:5432/ktzh"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL
# )
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# conn = engine.connect()
# Base = declarative_base()