from fastapi import FastAPI, Query
from random import randint

app = FastAPI()


@app.get('/')
def read_root():
    return {'Hello': 'World'}

@app.get('/about_me')
def show_about_me():
    return {
        'name': 'Vitaly',
        'age': '24',
        'group': 'T-323901-ИСТ'
    }

@app.get('/rnd')
def get_random_int():
    return randint(1, 10)

@app.post('/triangle')
def s_triangle(a: int = Query(gt=0), b: int = Query(gt=0), c: int = Query(gt=0)):
    if a + b <= c or a + c <= b or b + c <= a:
        return {'error': 'not exist'}
    
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c))**0.5
    return {'p_t': p,'s_t': s}