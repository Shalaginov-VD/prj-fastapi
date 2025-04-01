from fastapi import FastAPI, Query, Path, HTTPException
import pyd

app = FastAPI()

items = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 999.99,
        "description": "A powerful laptop for work and gaming."
    }
]


@app.get('/items/')
def read_item_list(name: str | None = Query(None, min_length=2),
    min_price: float | None = Query(None, gt=0),
    max_price: float | None = Query(None, gt=0),
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
        if name:
            if max_price < i['price']:
                continue
        k.append(i)
        
    return k[:limit]

@app.get('/items/{item_id}')
def read_item(item_id: int = Path(gt=0)):
    for i in items:
        if i['id'] == item.id:
            return i
    raise HTTPException(400, 'Товар не найден')

@app.post('/items/')
def create_item(item: items):
    item = dict(item)
    id = items[-1]['id'] + 1
    item['id'] = id
    items.append(item)
    return item