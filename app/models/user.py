from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime,timezone
from db.database import Base

class User(Base):

    __tablename__='users'

    id=Column(Integer,primary_key=True)
    username=Column(String,unique=True,nullable=False,index=True)
    email=Column(String,unique=True,nullable=False,index=True)
    hashed_password=Column(String,nullable=False)
    role=Column(String,default='user')
    created_at=Column(DateTime,default=lambda: datetime.now(timezone.utc))
    updated_at=Column(DateTime,default=lambda: datetime.now(timezone.utc),onupdate=lambda: datetime.now(timezone.utc))

    #relationship
    cart = relationship("Cart",back_populates="user",uselist=False)
    orders =  relationship("Order",back_populates="user")