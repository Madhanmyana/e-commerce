from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from schemas.order import OrderItemResponse,OrderResponse
from services.order_services import place_order
from dependencies.dependencies import get_current_user
from db.database import get_db

router=APIRouter()

@router.post("/orders")
def place_order(user=Depends(get_current_user),db:Session=Depends(get_db)):
    return place_order(user.id,db)