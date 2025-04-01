from pydantic import BaseModel, Field


class Item(BaseModel):
    name: str = Field(example='Ноутбук', min_length=2, max_length=100)
    price: float = Field(gt=0)
    description: str = Field(max_length=500)