from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from services.cart_services import get_cart,add_to_cart,update_cart_item,delete_cart_item,clear_cart
from schemas.cart import UpdateCartItemRequest,AddToCartRequest,CartItemResponse,CartResponse
from db.database import get_db
from dependencies.dependencies import get_current_user,require_admin

router=APIRouter()

@router.get('/cart')
def get_cart(user_id:int=Depends(get_current_user),db:Session=Depends(get_db)):
    return get_cart(user_id,db)

@router.post('/cart/items')
def add_item_to_cart(cart: AddToCartRequest, user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    return add_to_cart(user_id, cart, db)

@router.put('/cart/items{cart_item_id}')
def update_cart(cart_item_id:int ,cart:UpdateCartItemRequest, user_id:int=Depends(get_current_user), db:Session=Depends(get_db)):
    return update_cart_item(cart_item_id, user_id, cart, db)

@router.delete('/cart/items{cart_item_id}')
def delete_cart_item_by_id(cart_item_id: int, user_id:int=Depends(get_current_user) , db:Session=Depends(get_db)):
    return delete_cart_item(cart_item_id, user_id, db)

@router.delete('/cart/items')
def clear_cart_items(user_id: int=Depends(get_current_user), db: Session=Depends(get_db)):
    return clear_cart()