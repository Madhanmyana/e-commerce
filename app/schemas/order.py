from pydantic import BaseModel, ConfigDict
from datetime import datetime
from app.models.order import OrderStatus

#request schema
class UpdateOrderStatusRequest(BaseModel):
    status: OrderStatus

# response schema
class OrderItemResponse(BaseModel):
    id:int
    product_name:str
    price:float
    quantity:int
    model_config = ConfigDict(from_attributes=True)

class OrderResponse(BaseModel):
    id: int
    total: float
    status: str
    created_at: datetime
    items: list[OrderItemResponse]

    model_config = ConfigDict(from_attributes=True)