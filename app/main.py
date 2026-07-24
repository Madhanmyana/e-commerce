from fastapi import FastAPI

import models
from db.database import session,engine
from api.user import router as user_router
from api.product import router as product_router
from api.category import router as category_router

app=FastAPI()

#database
models.user.Base.metadata.create_all(bind=engine)
models.product.Base.metadata.create_all(bind=engine)

app.include_router(user_router)

app.include_router(product_router)

app.include_router(category_router)