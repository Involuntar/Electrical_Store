from pydantic import BaseModel, Field


class BaseProduct(BaseModel):
    id:int=Field(example=1)
    product_name:str=Field(example="Самсунг")
    product_price:float=Field(example=86000)
    description:str|None=Field(example="Описание")
    amount:int=Field(example=500)


class BaseCategory(BaseModel):
    id:int=Field(example=1)
    category_name:str=Field(example='Телефон')
