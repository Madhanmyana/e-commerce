import os
from dotenv import load_dotenv

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

load_dotenv()

DATA_BASE_URL=os.getenv("DATA_BASE_URL")
engine=create_engine(url=DATA_BASE_URL)
session=sessionmaker(autoflush=False,autocommit=False,bind=engine)

def get_db():

    db=session()

    try:
        yield db
    finally:
        db.close()