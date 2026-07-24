from pydantic import BaseModel,ConfigDict
from datetime import datetime

#request schema
# product
class ProductCreate(BaseModel):
    name:str
    description:str
    price:float
    stock:int
    category_id:int

class ProductUpdate(BaseModel):
    name:str
    description:str
    price:float
    stock:int
    category_id:int

# category
class CategoryCreate(BaseModel):
    name:str
    description:str

class CategoryUpdate(BaseModel):
    name:str
    description:str


#response schema
# product
class CategorySummaryResponse(BaseModel):
    id:int
    name:str
    description:str
    model_config = ConfigDict(from_attributes=True)

class ProductResponse(BaseModel):
    id:int
    name:str
    description:str
    price:float
    stock:int
    created_at:datetime
    updated_at:datetime
    category: CategorySummaryResponse
    model_config = ConfigDict(from_attributes=True)

class GetAllProductsResponse(BaseModel):
    page: int
    limit: int
    total: int
    total_pages: int
    products: list[ProductResponse]

# category
class ProductSummaryResponse(BaseModel):
    id:int
    name:str
    price:float
    model_config = ConfigDict(from_attributes=True)

class CategoryResponse(BaseModel):
    id:int
    name:str
    description:str
    created_at:datetime
    updated_at:datetime
    products:list[ProductSummaryResponse]
    model_config = ConfigDict(from_attributes=True)

class GetAllCategoriesResponse(BaseModel):
    categories:list[CategoryResponse]