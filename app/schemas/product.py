from pydantic import BaseModel

#request schema
class ProductCreate():
    name:str
    description:str
    price:float
    stock:int

#response schema
class ProductResponse():
    name:str
    description:str
    price:float
    stock:int

class ProductUpdate():
    name:str
    description:str
    price:float
    stock:int