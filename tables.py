from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *
from sqlalchemy.schema import ForeignKey
from pydantic import BaseModel
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:123@localhost/postgres"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base = declarative_base()

datab = SQLAlchemy()
class Categories(Base):
    __tablename__ = "categories"
    category_id = Column(Integer, primary_key=True, index=True)
    category_name = Column(String)


class SubCategories(Base):
    __tablename__ = "subcategories"
    subcategories_id = Column(Integer, primary_key=True, index=True)
    subcategories = Column(String)
    category_id = Column(Integer, ForeignKey('categories.category_id'))


class Items(Base):
    __tablename__ = "item"
    item_id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String)
    subcategory_id = Column(Integer)
    image = Column(String)
    description = Column(String)


# class CategoriesSchema(BaseModel):
#     category_id: int
#     category_name: str


# class SubCategoriesSchema(BaseModel):
#     subCategories_id: int
#     subCategories: str
#     categori_id: int


SessionLocal = sessionmaker(autoflush=False, bind=engine)

