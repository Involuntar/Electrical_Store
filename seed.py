from sqlalchemy.orm import Session
from database import engine
import models as m
import bcrypt


m.Base.metadata.drop_all(bind=engine)
m.Base.metadata.create_all(bind=engine)

with Session(bind=engine) as session:
    c1 = m.Category(category_name="Смартфон")
    c2 = m.Category(category_name="Телевизор")
    c3 = m.Category(category_name="Наушники")
    
    session.add(c1)
    session.add(c2)
    session.add(c3)

    s1 = m.Status(status_name="Собираем заказ")
    s2 = m.Status(status_name="Доставляем")
    s3 = m.Status(status_name="Заказ доставлен")

    session.add(s1)
    session.add(s2)
    session.add(s3)

    u1 = m.User(firstname="Иван", lastname="Иванов", username="1v4n", password=bcrypt.hashpw(b"pass", bcrypt.gensalt()))
    session.add(u1)

    p1 = m.Product(product_name="Самсунг", product_price="86000", 
                category_id="1", amount="500")
    p2 = m.Product(product_name="Айфон", product_price="64000", 
                category_id="1", amount="600")
    
    session.add(p1)
    session.add(p2)

    session.commit()