from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime,timezone

Base=declarative_base()

class User(Base):

    __tablename__='users'

    id=Column(Integer,primary_key=True)
    username=Column(String,unique=True,nullable=False,index=True)
    email=Column(String,unique=True,nullable=False,index=True)
    hashed_password=Column(String,nullable=False)
    role=Column(String,default='user')
    created_at=Column(DateTime,default=lambda: datetime.now(timezone.utc))
    updated_at=Column(DateTime,default=lambda: datetime.now(timezone.utc),onupdate=lambda: datetime.now(timezone.utc))
