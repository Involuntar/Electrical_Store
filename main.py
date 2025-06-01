from fastapi import FastAPI, HTTPException, Depends, Query
from database import get_db
from sqlalchemy.orm import Session
import models as m
from typing import List
import pyd


app=FastAPI()

# Товары
# Получение товара
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
    all_product = products.all()
    if not all_product:
        raise HTTPException(404, "Товары не найдены!")
    return all_product

# Создание товара
@app.post("/api/product", response_model=pyd.SchemeProduct)
def create_product(product:pyd.CreateProduct, db:Session=Depends(get_db)):
    product_dublicate = db.query(m.Product).filter(
        m.Product.product_name == product.product_name
    ).first()
    if product_dublicate:
        raise HTTPException(400, "Такой товар уже существует!")
    product_db = m.Product()
    product_db.product_name = product.product_name
    product_db.product_price = product.product_price
    product_db.category_id = product.category_id
    product_db.description = product.description
    product_db.amount = product.amount

    db.add(product_db)
    db.commit()
    return product_db


# Изменение товара
@app.put("/api/product/{id}", response_model=pyd.SchemeProduct)
def update_product(id:int, product:pyd.CreateProduct, db:Session=Depends(get_db)):
    product_db = db.query(m.Product).filter(
        m.Product.id == id
    ).first()
    if not product_db:
        raise HTTPException(404, "Товар не найден!")
    product_db.product_name = product.product_name
    product_db.product_price = product.product_price
    product_db.category_id = product.category_id
    product_db.description = product.description
    product_db.amount = product.amount

    db.add(product_db)
    db.commit()
    return product_db

# Удаление товара
@app.delete("/api/product/{id}")
def delete_product(id:int, db:Session=Depends(get_db)):
    product_db = db.query(m.Product).filter(
        m.Product.id == id
    ).first()
    if not product_db:
        raise HTTPException(404, "Товар не найден!")
    db.delete(product_db)
    db.commit()
    return {"detail": "Товар удалён!"}


# Заказы
# Получение заказа
@app.get("/api/orders", response_model=List[pyd.SchemeOrder])
def get_orders(db:Session=Depends(get_db)):
    orders = db.query(m.Order).all()
    return orders