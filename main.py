from fastapi import FastAPI, Query, Path, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

items = [
    {
        'id': 1,
        'name': 'Ноутбук',
        'price': 999.99,
        'description': 'Мощный ноутбук для работы и игр.'
    },
    {
        'id': 2,
        'name': 'Смартфон',
        'price': 888.88,
        'description': 'Новейший смартфон с передовыми функциями.'
    },
    {
        'id': 3,
        'name': 'Наушники',
        'price': 555.55,
        'description': 'Высококачественные наушники для любителей музыки.'
    }
]

class Items(BaseModel):
    name: str = Field(example='Ноутбук', min_length=2, max_length=100)
    price: float = Field(example='99.99', gt=0)
    description: str | None = Field(None, example='Мощный ноутбук для работы и игр.', max_length=500)

@app.get('/items/', response_model=List[Items])
def get_items(name: str | None = Query(None, min_length=2, example='Ноутбук'),
    min_price: float | None = Query(None, gt=0, example=100),
    max_price: float | None = Query(None, gt=0, example=1000),
    limit: int = Query(10, lt=100)
):
    if max_price and min_price:
        if max_price < min_price:
            raise HTTPException(400, 'Максимальная цена не может быть меньше минимальной')
    k = []
    for i  in items:
        if name:
            if name != i['name']:
                continue
        if min_price:
            if min_price > i['price']:
                continue
        if max_price:
            if max_price < i['price']:
                continue
        k.append(i)
        
    return k[:limit]

@app.get('/items/{item_id}', response_model=Items)
def get_item_id(item_id: int = Path(gt=0, example=42)):
    for i in items:
        if i['id'] == item_id:
            return i
    raise HTTPException(400, 'Товар не найден')

@app.post('/items/', response_model=Items)
def create_item(item: Items):
    item = dict(item)
    id = items[-1]['id'] + 1
    item['id'] = id
    items.append(item)
    return item