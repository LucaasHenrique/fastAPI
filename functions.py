import mysql.connector as my
from config import DB_CONFIG

def connect():
    conn = my.connect(
            **DB_CONFIG)
    return conn


def adicionarProduto(nome, preco):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(f'INSERT INTO frutas (nome, preço) SELECT "{nome}", {preco} FROM dual WHERE NOT EXISTS (SELECT 1 FROM frutas WHERE nome = "{nome}")')
    conn.commit()
    conn.close()


def lerProduto(id=0, nome=''):
    if id != 0 and nome == '':
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM frutas WHERE idfrutas = "{id}"')
        prod = cursor.fetchall()
        conn.close()
        return prod
    
    elif id == 0 and nome != '':
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM frutas WHERE nome = "{nome}"')
        prod = cursor.fetchall()
        conn.close()
        return prod


def updateItem(id, new_name, new_price):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(f'UPDATE frutas SET nome = "{new_name}", preço = "{new_price}" WHERE idfrutas = "{id}"')
    conn.commit()
    conn.close()


def deleteProduto(id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(f'DELETE FROM frutas WHERE idfrutas = "{id}"')
    conn.commit()
    conn.close()

