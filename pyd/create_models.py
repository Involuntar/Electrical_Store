from pydantic import BaseModel, Field
from datetime import date, datetime

class CreateProduct(BaseModel):
    product_name:str=Field(example="Самсунг")
    product_price:float=Field(example=86000)
    description:str|None=Field(example="Описание", default=None)
    category_id:int=Field(example="1")
    amount:int=Field(example=500)

class CreateOrder(BaseModel):
    summ:float=Field(example=21673, ge=0)
    order_date:date=Field(example="2025-06-11", default=datetime.now().strftime("%Y-%m-%d"))
    user_id:int=Field(example=1)
    status_id:int=Field(example=1, default=1)

class CreateReview(BaseModel):
    rating:float=Field(example=4.5, ge=0, le=5)
    description:str|None=Field(example="Хороший товар!", default=None)
    product_id:int=Field(example=1)
    user_id:int=Field(example=1)