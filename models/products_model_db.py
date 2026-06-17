from core.database import Base , engine
from sqlalchemy import Column, Integer, String , Boolean


class Product(Base):
    __tablename__  = "product"

    id = Column(Integer, index=True, primary_key=True)
    product_name = Column(String(50), index=True, unique=True)
    price = Column(Integer, index=True)
    description = Column(String(200), index=True)

Base.metadata.create_all(bind=engine)
