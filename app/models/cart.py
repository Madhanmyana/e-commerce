from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, DateTime,Float,ForeignKey
from datetime import datetime,timezone

from db.database import Base

class Cart(Base):

    __tablename__='cart'

    id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey('users.id'),nullable=False,unique=True)
    created_at=Column(DateTime,default=lambda:datetime.now(timezone.utc))
    updated_at=Column(DateTime,default=lambda:datetime.now(timezone.utc),onupdate=lambda:datetime.now(timezone.utc))

    #relationship
    user = relationship("User",back_populates="cart")
    items = relationship("CartItem",back_populates="cart")

class CartItem(Base):

    __tablename__='cartitem'

    id=Column(Integer,primary_key=True)
    cart_id=Column(Integer,ForeignKey('cart.id'))
    product_id=Column(Integer,ForeignKey('product.id'))
    quantity=Column(Integer)
    created_at=Column(DateTime,default=lambda:datetime.now(timezone.utc))
    updated_at=Column(DateTime,default=lambda:datetime.now(timezone.utc),onupdate=lambda:datetime.now(timezone.utc))

    #relationship
    cart = relationship("Cart",back_populates="items")
    product = relationship("Product",back_populates="cart_items")