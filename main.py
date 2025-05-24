from fastapi import FastAPI, HTTPException, Depends
from database import get_db
from sqlalchemy.orm import Session
import models as m
from typing import List
import pyd


app=FastAPI()

# Товары
@app.get("/api/products", response_model=List[pyd.SchemeProduct])
def get_products(db:Session=Depends(get_db)):
    products = db.query(m.Product).all()
    return products