from fastapi import FastAPI

from app import models
from db.database import session,engine,Base
from api.user import router as user_router
from api.product import router as product_router
from api.category import router as category_router
from api.cart import router as cart_router
from api.order import router as order_router
from api.health import router as health_router

app=FastAPI()

#database
Base.metadata.create_all(bind=engine)

#api router
app.include_router(user_router)
app.include_router(product_router)
app.include_router(category_router)
app.include_router(cart_router)
app.include_router(order_router)
app.include_router(health_router)