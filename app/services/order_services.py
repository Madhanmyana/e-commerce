from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.order import Order, OrderItem
from app.models.cart import Cart, CartItem
from app.models.product import Product
from app.schemas.order import UpdateOrderStatusRequest

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

def get_orders(user_id:int,db:Session):
    orders=db.query(Order).filter(Order.user_id==user_id).all()

    return {
        'orders':orders
    }

def get_order_by_id(user_id:int,order_id:int,db:Session):
    order=db.query(Order).filter(Order.user_id==user_id,Order.id==order_id).first()

    if not order:
        raise HTTPException(status_code=404,detail='order not found')

    return{
        'order':order
    }

def update_order_status(order_id:int,update: UpdateOrderStatusRequest,db:Session):
    order=db.query(Order).filter(Order.id==order_id).first()

    if not order:
        raise HTTPException(status_code=404,detail='order not found')

    order.status=update.status
    db.commit()
    db.refresh(order)

    return{
        'order_id':order.id,
        'status':order.status
    }