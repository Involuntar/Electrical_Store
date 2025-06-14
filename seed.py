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

    r1 = m.Role(role_name="Покупатель")
    r2 = m.Role(role_name="Менеджер")
    r3 = m.Role(role_name="Админ")

    session.add(r1)
    session.add(r2)
    session.add(r3)

    u1 = m.User(firstname="Иван", lastname="Иванов", username="1v4n", password=bcrypt.hashpw(b"KaX8inFbp!SC11", bcrypt.gensalt()), role_id=1)
    u2 = m.User(firstname="Иван", lastname="Иванов", username="Van", password=bcrypt.hashpw(b"eoAz%yye0wXD6W", bcrypt.gensalt()), role_id=2)
    u3 = m.User(firstname="Иван", lastname="Иванов", username="Vanya", password=bcrypt.hashpw(b"Qb@zwkmc#Bf6Wf", bcrypt.gensalt()), role_id=3)

    session.add(u1)
    session.add(u2)
    session.add(u3)

    p1 = m.Product(product_name="Самсунг", product_price="86000", 
                category_id="1", amount="500")
    p2 = m.Product(product_name="Айфон", product_price="64000", 
                category_id="1", amount="600")
    
    session.add(p1)
    session.add(p2)

    session.commit()