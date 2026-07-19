from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, DateTime,Float
from datetime import datetime,timezone

Base=declarative_base()

class Product(Base):

    __tablename__='product'

    id=Column(Integer,primary_key=True)
    name=Column(String,index=True,nullable=False)
    description=Column(String)
    price=Column(Float,nullable=False)
    stock=Column(Integer,nullable=False)
    created_at=Column(DateTime,default=lambda:datetime.now(timezone.utc))
    updated_at=Column(DateTime,default=lambda:datetime.now(timezone.utc),onupdate=lambda:datetime.now(timezone.utc))