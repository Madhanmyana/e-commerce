from sqlalchemy import Column,Integer,Float,String,DateTime,ForeignKey,Enum
from sqlalchemy.orm import relationship
from datetime import datetime,timezone
from enum import Enum as pyEnum


from db.database import Base

class OrderStatus(str,pyEnum):
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    SHIPPED = "Shipped"
    DELIVERED = "Delivered"
    CANCELLED = "Cancelled"

class Order(Base):

    __tablename__='order'

    id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey('users.id'))
    total=Column(Float,nullable=False)
    status=Column(Enum(OrderStatus),default=OrderStatus.PENDING,nullable=False)
    created_at=Column(DateTime,default=lambda:datetime.now(timezone.utc))
    updated_at=Column(DateTime,default=lambda:datetime.now(timezone.utc),onupdate=lambda:datetime.now(timezone.utc))

    #relationship
    user=relationship("User",back_populates="orders")
    items=relationship("OrderItem",back_populates="order")

class OrderItem(Base):

    __tablename__='orderitem'

    id=Column(Integer,primary_key=True)
    order_id=Column(Integer,ForeignKey('order.id'))
    product_id=Column(Integer,ForeignKey('product.id'))
    product_name=Column(String)
    price=Column(Float)
    quantity=Column(Integer)

    #relationship
    order=relationship("Order",back_populates="items")
    product=relationship("Product",back_populates="order_items")