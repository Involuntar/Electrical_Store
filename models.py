from database import Base
from sqlalchemy import Column, Integer, String, Float, DECIMAL, ForeignKey, Text, Date
from sqlalchemy.orm import relationship


class Category(Base):
    __tablename__="categories"
    id = Column(Integer, primary_key=True, autoincrement=True)
    category_name = Column(String(20))


class Product(Base):
    __tablename__="products"
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String(50), unique=True)
    product_price = Column(DECIMAL(10, 2), default=0)
    category_id = Column(Integer, ForeignKey("categories.id"))
    description = Column(Text, nullable=True)
    amount = Column(Integer, default=0)

    category = relationship("Category", backref="products")

class User(Base):
    __tablename__="users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(20))
    lastname = Column(String(20))
    username = Column(String(20))
    password = Column(String(255))


class Status(Base):
    __tablename__="statuses"
    id = Column(Integer, primary_key=True, autoincrement=True)
    status_name = Column(String(20))


class Order(Base):
    __tablename__="orders"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    status_id = Column(Integer, ForeignKey("statuses.id"))
    summ = Column(DECIMAL(10, 2))
    order_date = Column(Date)

    user = relationship("User", backref="orders")
    status = relationship("Status", backref="orders")


class Review(Base):
    __tablename__="reviews"
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    rating = Column(Float)
    description = Column(Text, nullable=True)

    product = relationship("Product", backref="reviews")
    user = relationship("User", backref="reviews")