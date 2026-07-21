from pydantic import BaseModel

#request schema
class ProductCreate(BaseModel):
    name:str
    description:str
    price:float
    stock:int

#response schema
class ProductResponse(BaseModel):
    name:str
    description:str
    price:float
    stock:int

class ProductUpdate(BaseModel):
    name:str
    description:str
    price:float
    stock:int

class GetAllProductsResponse(BaseModel):
    page: int
    limit: int
    total: int
    total_pages: int
    products: list[ProductResponse]