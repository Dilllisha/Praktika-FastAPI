import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *
from sqlalchemy.schema import ForeignKey


engine = sqlalchemy.create_engine("postgresql://postgres:123@localhost/postgres")
conn = engine.connect()
metadata = sqlalchemy.MetaData()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()
Base = declarative_base()


class Categories(Base):
    __tablename__ = "categories"
    category_id = Column(Integer, primary_key=True)
    category_name = Column(String)


class SubCategories(Base):
    __tablename__ = "subcategories"
    subcategories_id = Column(Integer, primary_key=True)
    subcategories = Column(String)
    category_id = Column(Integer, ForeignKey('categories.category_id'))


class Items(Base):
    __tablename__ = "item"
    item_id = Column(Integer, primary_key=True)
    item_name = Column(String)
    subcategory_id = Column(Integer)
    image = Column(String)
    description = Column(String)