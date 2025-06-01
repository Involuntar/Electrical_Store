from pydantic import BaseModel, Field


class CreateProduct(BaseModel):
    product_name:str=Field(example="Самсунг")
    product_price:float=Field(example=86000)
    description:str|None=Field(example="Описание", default=None)
    category_id:int=Field(example="1")
    amount:int=Field(example=500)

