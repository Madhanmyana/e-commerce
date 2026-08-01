from pydantic import BaseModel,ConfigDict

#request schema
class AddToCartRequest(BaseModel):
    product_id:int
    quantity:int
    
class UpdateCartItemRequest(BaseModel):
    quantity:int

#response schema
class CartItemSummaryResponse(BaseModel):
    id:int
    name:str
    price:float
    model_config = ConfigDict(from_attributes=True)

class CartItemResponse(BaseModel):
    product:CartItemSummaryResponse
    quantity:int
    model_config = ConfigDict(from_attributes=True)

class CartResponse(BaseModel):
    items:list[CartItemResponse]
    model_config = ConfigDict(from_attributes=True)