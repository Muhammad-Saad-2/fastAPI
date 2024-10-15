from sqlalchemy import Column, Integer, Boolean, String
from sqlalchemy.orm  import declarative_base

Base = declarative_base()

class TodoItem(Base):
    __tablename__ = "Todos"
    id = Column(Integer,primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index = True)
    status=Column(Boolean)

