from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from app.services.cart_services import get_cart as get_cart_service,add_to_cart,update_cart_item,delete_cart_item,clear_cart
from app.schemas.cart import UpdateCartItemRequest,AddToCartRequest,CartItemResponse,CartResponse
from app.db.database import get_db
from app.dependencies.dependencies import get_current_user,require_admin

router=APIRouter()

@router.get('/cart',response_model=CartResponse)
def get_cart(user_id=Depends(get_current_user),db:Session=Depends(get_db)):
    return get_cart_service(user_id.id,db)

@router.post('/cart/items',response_model=CartItemResponse)
def add_item_to_cart(cart: AddToCartRequest, user_id= Depends(get_current_user), db: Session = Depends(get_db)):
    return add_to_cart(user_id.id, cart, db)

@router.put('/cart/items/{cart_item_id}',response_model=CartResponse)
def update_cart(cart_item_id:int ,cart:UpdateCartItemRequest, user_id=Depends(get_current_user), db:Session=Depends(get_db)):
    return update_cart_item(cart_item_id, cart, user_id.id, db)

@router.delete('/cart/items/{cart_item_id}',response_model=CartResponse)
def delete_cart_item_by_id(cart_item_id: int, user_id=Depends(get_current_user) , db:Session=Depends(get_db)):
    return delete_cart_item(cart_item_id, user_id.id, db)

@router.delete('/cart/items',response_model=CartResponse)
def clear_cart_items(user_id=Depends(get_current_user), db: Session=Depends(get_db)):
    return clear_cart(user_id.id, db)