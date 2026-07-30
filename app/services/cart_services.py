from fastapi import HTTPException
from sqlalchemy.orm import Session

from schemas.cart import AddToCartRequest,UpdateCartItemRequest
from models.product import Product
from models.cart import Cart,CartItem


def get_cart(user_id:int,db:Session):
    if Cart.user_id==user_id:
        return {
            'items':cart.items
        }

    return{
        'items':[]
    }

def add_to_cart(user_id: int, cart: AddToCartRequest, db: Session):
    if cart.quantity>0:
        if db.query(Product).filter(Product.id==cart.product_id).first():
            user_cart=db.query(Cart).filter(Cart.user_id == user_id).first()
            if not user_cart:
                new_cart=Cart(
                    user_id=user_id
                )

                db.add(new_cart)
                db.commit()
                db.refresh(new_cart)
                user_cart=new_cart

            existing_cart_item=db.query(CartItem).filter(CartItem.cart_id==user_cart.id,CartItem.product_id==cart.product_id).first()
            if existing_cart_item:
                existing_cart_item.quantity+=cart.quantity
                db.commit()
                db.refresh(existing_cart_item)
            else:
                new_cart_item=CartItem(
                    cart_id=user_cart.id,
                    product_id=cart.product_id,
                    quantity=cart.quantity
                )
                db.add(new_cart_item)
                db.commit()
                db.refresh(new_cart_item)
            return {
                "items": user_cart.items
                }

        raise HTTPException(status_code=404,detail='product not found')
    raise HTTPException(status_code=400,detail='bad request')

def update_cart_item(cart_item_id: int, cart: UpdateCartItemRequest, user_id: int, db: Session):
    if cart.quantity <= 0:
        raise HTTPException(status_code=400, detail="Invalid quantity")

    user_cart = db.query(Cart).filter(Cart.user_id == user_id).first()

    if not user_cart:
        raise HTTPException(status_code=404, detail="Cart not found")

    existing_cart_item = db.query(CartItem).filter(CartItem.id == cart_item_id,CartItem.cart_id == user_cart.id).first()

    if not existing_cart_item:
        raise HTTPException(status_code=404,detail="Cart item not found")

    existing_cart_item.quantity = cart.quantity

    db.commit()
    db.refresh(existing_cart_item)

    return {
        "items": user_cart.items
    }

def delete_cart_item(cart_item_id: int, user_id: int, db: Session):

    user_cart = db.query(Cart).filter(Cart.user_id == user_id).first()

    if not user_cart:
        raise HTTPException(status_code=404, detail="Cart not found")
    
    existing_cart_item = db.query(CartItem).filter(CartItem.id == cart_item_id,CartItem.cart_id == user_cart.id).first()

    if not existing_cart_item:
        raise HTTPException(status_code=404,detail="Cart item not found")
    
    db.delete(existing_cart_item)
    db.commit()
    return {
        "items": user_cart.items
    }

def clear_cart(user_id: int, db: Session):

    user_cart = db.query(Cart).filter(Cart.user_id == user_id).first()

    if not user_cart:
        raise HTTPException(status_code=404, detail="Cart not found")
    
    existing_cart_items = db.query(CartItem).filter(CartItem.cart_id == user_cart.id).all()

    if not existing_cart_items:
        return {
        "items": []
    }
    else:
        for items in existing_cart_items:
            db.delete(items)
            
        db.commit()
        return {
            "items": []
        }