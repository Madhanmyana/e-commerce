from fastapi import FastAPI

from db.database import session,engine
import models.user
from api.user import router as user_router

app=FastAPI()

models.user.Base.metadata.create_all(bind=engine)

app.include_router(user_router)