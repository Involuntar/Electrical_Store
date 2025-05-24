from database import Base
from sqlalchemy import Column, Integer, String, Float, DECIMAL, ForeignKey, Text, Date


class Category(Base):
    __tablename__="categories"
    id = Column(Integer, primary_key=True, autoincrement=True)
    category_name = Column(String(20))


class Good(Base):
    __tablename__="goods"
    id = Column(Integer, primary_key=True, autoincrement=True)
    good_name = Column(String(50), unique=True)
    good_price = Column(DECIMAL(10, 2), default=0)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    description = Column(Text, nullable=True)
    amount = Column(Integer, default=0)


class User(Base):
    __tablename__="users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(20))
    lastname = Column(String(20))
    username = Column(String(20))
    password = Column(String(20))


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
    date = Column(Date)


class Review(Base):
    __tablename__="reviews"
    id = Column(Integer, primary_key=True, autoincrement=True)
    good_id = Column(Integer, ForeignKey("goods.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    rating = Column(Float)
    description = Column(Text, nullable=True)