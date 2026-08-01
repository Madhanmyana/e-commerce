from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.order import Order, OrderItem
from models.cart import Cart, CartItem
from models.product import Product

def place_order(user_id:int,db:Session):

    user_cart = db.query(Cart).filter(Cart.user_id == user_id).first()

    # if not user_cart:
    #     raise HTTPException(status_code=404,detail="cart not found")

    existing_cart_items = db.query(CartItem).filter(CartItem.cart_id == user_cart.id).all()

    if not existing_cart_items:
        raise HTTPException(status_code=404,detail="cart is empty")

    total=0
    for item in existing_cart_items:
        product = db.query(Product).filter(Product.id == item.product_id).first()

        if not product:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        if product.stock < item.quantity:
            raise HTTPException(
                status_code=400,
                detail=f"Insufficient stock for {product.name}"
            )
        
        total += product.price * item.quantity
    
    new_order = Order(user_id=user_id,total=total)
    db.add(new_order)
    db.flush()

    for item in existing_cart_items:
        product = db.query(Product).filter(Product.id == item.product_id).first()

        order_item=OrderItem(order_id=new_order.id,
                            product_id=item.product_id,
                            product_name=product.name,
                            price=product.price,
                            quantity=item.quantity)
        
        db.add(order_item)

        product.stock= product.stock-item.quantity
        db.delete(item)

    db.commit()
    db.refresh(new_order)
    
    return {
        'id':new_order.id,
        'total':total,
        'items':new_order.items
    }