from sqlalchemy.orm import Session
from database import engine
import models as m


m.Base.metadata.drop_all(bind=engine)
m.Base.metadata.create_all(bind=engine)

with Session(bind=engine) as session:
    c1 = m.Category(category_name="Телефон")
    session.add(c1)

    p1 = m.Product(product_name="Самсунг", product_price="86000", 
                category_id="1", amount="500")
    session.add(p1)

    p2 = m.Product(product_name="Айфон", product_price="64000", 
                category_id="1", amount="600")
    session.add(p2)

    session.commit()