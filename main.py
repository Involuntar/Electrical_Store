from fastapi import FastAPI, HTTPException, Depends, Query
from database import get_db
from sqlalchemy.orm import Session
import models as m
from typing import List
import pyd


app=FastAPI()

# Товары
@app.get("/api/products", response_model=List[pyd.SchemeProduct])
def get_products(limit:None|int=Query(None), page:None|int=Query(1), category:None|int=Query(None), minPrice:None|float=Query(None), db:Session=Depends(get_db)):
    products = db.query(m.Product)
    if category:
        products = products.filter(
            m.Product.category_id == category
        )
    if minPrice:
        products = products.filter(
            m.Product.product_price >= minPrice
        )
    if limit:
        products = products[(page - 1) * limit:page * limit]
    return products