from pydantic import BaseModel, Field
from datetime import date


class BaseProduct(BaseModel):
    id:int=Field(example=1)
    product_name:str=Field(example="Самсунг")
    product_price:float=Field(example=86000)
    description:str|None=Field(example="Описание")
    amount:int=Field(example=500)


class BaseCategory(BaseModel):
    id:int=Field(example=1)
    category_name:str=Field(example='Телефон')


class BaseOrder(BaseModel):
    id:int=Field(example=1)
    summ:float=Field(example=21673)
    order_date:date=Field(example="2025-06-11")


class BaseUser(BaseModel):
    id:int=Field(example=1)
    firstname:str=Field(example="Иван")
    lastname:str=Field(example="Иванов")
    username:str=Field(example="1v4n")


class BaseRole(BaseModel):
    id:int=Field(example=1)
    role_name:str=Field(example="Покупатель")

class BaseStatus(BaseModel):
    id:int=Field(example=1)
    status_name:str=Field(example="В доставке")


class BaseReview(BaseModel):
    id:int=Field(example=1)
    rating:float=Field(example=4.5)
    description:str|None=Field(example="Хороший товар!")
