from pydantic import BaseModel
from fastapi import FastAPI
from typing import Optional
import functions as fun
import mysql.connector as my

app = FastAPI()

class Item(BaseModel):
    nome: str
    preço: float 


class UpdateItem(BaseModel):
    nome: str = None
    preço: float = None 


@app.get('/')
def home():
    return {'msg': 'API está no ar'}

@app.get('/get-Item/{id}')
def getItem(id: int):
    search = fun.lerProduto(id=id)
    return {'nome': search[0][1], 'preço': search[0][2]}

@app.get('/get-by-name/{name}')
def getName(name):
    search = fun.lerProduto(nome=name)
    return {'nome': search[0][1], 'preço': search[0][2]}

@app.post('/add-item')
def createItem(item: Item):
    try:
        fun.adicionarProduto(item.nome, item.preço)
        return {'nome': item.nome, 'preço': item.preço}
    except Exception as e:
        return {'error': str(e)}

@app.put('/updata-item')
def updateItem(id: int, item: UpdateItem):
    try:
        fun.updateItem(id, item.nome, item.preço)
        search = fun.lerProduto(id)
        return {'nome': search[0][1], 'preço': search[0][2]} 
    except Exception as e:
        return {'error': str(e)}

@app.delete('/delete')
def deleteItem(id: int):
    try:
        search = fun.lerProduto(id)
        fun.deleteProduto(id)
        return {'nome': search[0][1], 'preço': search[0][2]}
    except Exception as e:
        return {'error': str(e)}
