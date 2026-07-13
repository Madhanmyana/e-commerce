from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.product import Product
from schemas.product import ProductCreate, ProductResponse, ProductUpdate

def product_create(product:ProductCreate,db:Session):
    if not db.query(Product).filter(Product.name==product.name):
        raise HTTPException(status_code=400,detail='product alredy exist')
    
    new_product=Product(
        name=product.name,
        description=product.description,
        price=product.price,
        stock=product.stock
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product