from core.database import Base , engine
from sqlalchemy import Integer, String, Column, Boolean, Date, DateTime
from datetime import datetime

class Admin(Base):
    __tablename__  = "admin"

    id = Column(Integer, index=True, primary_key=True)
    name_admin = Column(String(100), index=True)
    email = Column(String(50), index=True, unique=True)
    user_name = Column(String(50), index=True)
    password = Column(String(18), index=True)
    is_root_admin = Column(Boolean(True))
    changer_access = Column(Boolean(True))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


Base.metadata.create_all(bind=engine)