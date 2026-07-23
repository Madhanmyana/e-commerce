from pydantic import BaseModel
from datetime import datetime

#request schema
# product
class ProductCreate(BaseModel):
    name:str
    description:str
    price:float
    stock:int

class ProductUpdate(BaseModel):
    name:str
    description:str
    price:float
    stock:int

# category
class CategoryCreate(BaseModel):
    name:str
    description:str

class CategoryUpdate(BaseModel):
    name:str
    description:str


#response schema
# product
class ProductResponse(BaseModel):
    id:int
    name:str
    description:str
    price:float
    stock:int
    created_at:datetime
    updated_at:datetime

class GetAllProductsResponse(BaseModel):
    page: int
    limit: int
    total: int
    total_pages: int
    products: list[ProductResponse]

# category
class CategoryResponse(BaseModel):
    id:int
    name:str
    description:str
    created_at:datetime
    updated_at:datetime

class GetAllCategoriesResponse(BaseModel):
    categories:list[CategoryResponse]