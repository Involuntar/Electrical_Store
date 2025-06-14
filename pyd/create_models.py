from pydantic import BaseModel, Field
from datetime import date, datetime
import re

class CreateProduct(BaseModel):
    product_name:str=Field(example="Самсунг", min_length=2)
    product_price:float=Field(example=86000, gt=0)
    description:str|None=Field(example="Описание", default=None)
    category_id:int=Field(example="1")
    amount:int=Field(example=500, ge=0)

class CreateOrder(BaseModel):
    summ:float=Field(example=21673, gt=0)
    order_date:date=Field(example="2025-06-11", default=datetime.now().strftime("%Y-%m-%d"))
    user_id:int=Field(example=1)
    status_id:int=Field(example=1, default=1)

class CreateReview(BaseModel):
    rating:float=Field(example=4.5, ge=0, le=5)
    description:str|None=Field(example="Хороший товар!", default=None)
    product_id:int=Field(example=1)
    user_id:int=Field(example=1)

class AcceptReview(BaseModel):
    accepted:bool=Field(example=True)

class CreateUser(BaseModel):
    firstname:str=Field(example="Иван", min_length=2)
    lastname:str=Field(example="Иванов", min_length=2)
    username:str=Field(example="1v4n", min_length=2, max_length=20)
    password:str=Field(example="1v4n", min_length=8, max_length=20, pattern=re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"))

class LoginUser(BaseModel):
    username:str=Field(example="1v4n", min_length=2, max_length=20)
    password:str=Field(example="1v4n", min_length=8, max_length=20, pattern=re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"))