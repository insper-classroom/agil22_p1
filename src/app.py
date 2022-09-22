from flask import Flask, request, jsonify
from pathlib import Path
from classes.rede_social import User, Timeline
import pandas as pd


app = Flask(__name__)
app.list_of_dicts = []

@app.before_first_request
def load_dados():
    usuario_c = User(user_id=1220)
    usuario_r = User(user_id=1221)
    usuario_b = User(user_id=1222)
    usuario_e = User(user_id=1223)
    usuario_ed = User(user_id=1, nome='Eduardo', email='eduardo@email.com')

# Apenas rota de teste, pode ser removida posteriormente
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

def buscar_produto_por_nome(nome):
    
    for prod in app.list_of_dicts:
        if nome.lower() == prod['name'].lower():
            return prod, True
        else:
            return None, False

def buscar_produto(ean):

    for prod in app.list_of_dicts:
        if ean == prod['ean']:
            return prod, True
        else:
            return None, False

def todos_produtos():
    
    i = 1
    resp = {}
    for prod in app.list_of_dicts[:1000]:
        resp[i] = prod
        i +=1

    return resp, True

@app.route('/produto/', methods=['POST'])
def rota_inserir_produto( ):

    try:
        content = request.get_json()
    except:
        return {'Erro': 'Entrada não é um Json Válido'}, 400

    resp, encontrado = buscar_produto_por_nome(content['name'])

    if not(encontrado):
        app.list_of_dicts.append(content)
        return {'Produto Cadastrado': content}, 201
    else:
        return {'Erro': 'Produto já existe no cadastro'}, 500


@app.route('/produto/<string:ean>', methods=['GET'])
def rota_buscar_produto( ean ):

    resp, sucesso = buscar_produto(ean)

    print(resp)
    if sucesso:
        return resp, 200
    else:
        return {'Erro': 'Produto não Encontrado'}, 404

@app.route('/produto/', methods=['GET'])
def rota_buscar_todos_produtos():

    resp, sucesso = todos_produtos()

    if sucesso:
        return resp, 200
    else:
        return {'Erro': 'Produto não'}, 404

@app.route('/produto/', methods=['PUT'])
def rota_alterar_produto( ):

    pass


if __name__ == '__main__':
    app.run(debug=True)