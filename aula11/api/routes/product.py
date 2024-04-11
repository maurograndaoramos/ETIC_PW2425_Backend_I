from fastapi import APIRouter, HTTPException
from faker import Faker
from api.models import Product

router = APIRouter(
    prefix="/product",
    tags=["product"],
)

def create_connection():
#     client = MongoClient('localhost', 8000) 
#     db = client['database_name']
#     return db
    pass

@router.get("")
async def get_all_products():

    total_rows = 20

    result = [
        Product(
            id=Faker().uuid4(),
            name=Faker().name(),
            price=Faker().random_number(digits=2),
            enabled=Faker().boolean(),
            sku=Faker().random_number(digits=3)
        )
        for _ in range(total_rows)
    ]

    return Product

#     connection = create_connection()
#     products = connection['products']

#     all_products = list(products.find())

#     if not all_products:
#         raise HTTPException(status_code=404, detail="No products found")

#     return all_products

# @router.get("/{product_id}")
# async def get_product(product_id: str):
#     connection = create_connection()
#     products = connection['products']

#     product = products.find_one({"id": product_id})

#     if not product:
#         raise HTTPException(status_code=404, detail="Product not found")

#     return product