from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from services.cart_services import get_cart,add_to_cart,update_cart_item
from schemas.cart import UpdateCartItemRequest,AddToCartRequest,CartItemResponse,CartResponse
from db.database import get_db
from dependencies.dependencies import get_current_user,require_admin

router=APIRouter()

@router.post('/cart')
def get_cart(user_id:int=Depends(get_current_user),db:Session=Depends(get_db)):
    return get_cart(user_id,db)

@router.post('/cart')
def add_item_to_cart(cart: AddToCartRequest, user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    return add_to_cart(user_id, cart, db)

@router.put('/cart{cart_item_id}')
def update_cart(cart:UpdateCartItemRequest, user_id:int=Depends(get_current_user), db:Session=Depends(get_db)):
    return update_cart_item(user_id, cart, db)
