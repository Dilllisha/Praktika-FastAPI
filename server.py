from sqlalchemy.orm import Session
from fastapi import *
from tables import *
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()
db = SessionLocal()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/items")
def get_items():
    items = db.query(Items).all()
    return items


# @app.get("/categories")
# def get_categories():
#     sub = db.query(SubCategories).join(Categories, SubCategories.category_id == Categories.category_id)
#     cat = db.query(Categories).join(SubCategories, SubCategories.category_id == Categories.category_id)
#     rec = cat.all(), sub.all()
#     return cat.all(), sub.all()

@app.get("/categories")
def get_categories():
    a = db.query(Categories).outerjoin(SubCategories, Categories.category_id  == SubCategories.category_id)
    #
    # return a.all()