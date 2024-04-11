from pydantic import BaseModel

class Product(BaseModel):
    name: str
    sku: str
    price: float
    enabled: bool
    id: int
    