from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from schemas.order import OrderItemResponse,OrderResponse,UpdateOrderStatusRequest
from services.order_services import place_order,get_orders,get_order_by_id,update_order_status
from dependencies.dependencies import get_current_user,require_admin
from db.database import get_db

router=APIRouter()

@router.post("/orders")
def place_order(user=Depends(get_current_user),db:Session=Depends(get_db)):
    return place_order(user.id,db)

@router.get("/orders")
def all_orders(user=Depends(get_current_user),db:Session=Depends(get_db)):
    return get_orders(user.id,db)

@router.get("/orders/{order_id}")
def order_by_id(order_id,status:UpdateOrderStatusRequest,user=Depends(get_current_user),db=Depends(get_db)):
    return get_order_by_id(user.id,order_id,status,db)

@router.get("/orders{order_id}")
def update_status(order_id:int,update: UpdateOrderStatusRequest,db:Session=Depends(get_db),admin=Depends(require_admin)):
    return update_order_status(order_id,update,db)