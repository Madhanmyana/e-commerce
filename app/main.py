from fastapi import FastAPI

from app import models
from app.db.database import session,engine,Base
from app.api.user import router as user_router
from app.api.product import router as product_router
from app.api.category import router as category_router
from app.api.cart import router as cart_router
from app.api.order import router as order_router
from app.api.health import router as health_router

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