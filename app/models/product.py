from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, String, Integer, DateTime,Float,ForeignKey
from datetime import datetime,timezone

Base=declarative_base()

class Product(Base):

    __tablename__='product'

    id=Column(Integer,primary_key=True)
    name=Column(String,index=True,nullable=False)
    description=Column(String)
    price=Column(Float,nullable=False)
    stock=Column(Integer,nullable=False)
    category_id=Column(Integer,ForeignKey('category.id'),nullable=False)
    created_at=Column(DateTime,default=lambda:datetime.now(timezone.utc))
    updated_at=Column(DateTime,default=lambda:datetime.now(timezone.utc),onupdate=lambda:datetime.now(timezone.utc))

    # relationship
    category = relationship("Category",back_populates="products")


class Category(Base):

    __tablename__='category'

    id=Column(Integer,primary_key=True)
    name=Column(String,index=True,nullable=False)
    description=Column(String)
    created_at=Column(DateTime,default=lambda:datetime.now(timezone.utc))
    updated_at=Column(DateTime,default=lambda:datetime.now(timezone.utc),onupdate=lambda:datetime.now(timezone.utc))

    #relationship
    products = relationship("Product",back_populates="category")