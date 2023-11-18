from fastapi import *
from tables import *
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()


origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/categories")
def get_categories():
    cat = (db.query(Categories).join(SubCategories, Categories.category_id == SubCategories.category_id)
           .filter(Categories.category_id == SubCategories.category_id))
    sub = (db.query(SubCategories).join(Categories, Categories.category_id == SubCategories.category_id)
           .filter(Categories.category_id == SubCategories.category_id))
    item = db.query(Items).join(SubCategories, Items.subcategory_id == SubCategories.subcategories_id)
    return cat.all(), sub.all(), item.all()

