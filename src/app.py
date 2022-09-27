from flask import Flask, request, jsonify
from pathlib import Path
from classes.rede_social import *
from model.db import *


app = Flask(__name__)

@app.before_first_request
def load_dados():
    usuario_c = User(user_id=1220)
    usuario_r = User(user_id=1221)
    usuario_b = User(user_id=1222)
    usuario_e = User(user_id=1223)
    usuario_ed = User(user_id=1, nome='Eduardo', email='eduardo@email.com')

    usuario_c.adicionar_amigo(usuario_b)
    usuario_c.adicionar_amigo(usuario_r)
    usuario_e.adicionar_amigo(usuario_b)

    post1_c = usuario_c.escrever_post('Meu primeiro Post - Camila')
    post2_c = usuario_c.escrever_post('Meu segundo Post - Camila')

    comentario_r_para_c_post_1 = usuario_r.comentar_post(post1_c, 'Comentario de Ramon no Post 1 de Camila')
    comentario_r_para_c_post_2 = usuario_r.comentar_post(post2_c, 'Comentario de Ramon no Post 2 de Camila')
    comentario_e_para_c_post_2 = usuario_e.comentar_post(post2_c, 'Comentario de Eliza no Post 2 de Camila')



# Apenas rota de teste, pode ser removida posteriormente
@app.route("/")
def hello_world():
    return "<p>Apenas um teste no dominio raiz!</p>"



# Operações com a base
@app.route('/usuario/<int:user_id>', methods=['POST'])
def rota_inserir_usuario( user_id ):

    try:
        content = request.get_json()
    except:
        return {'Erro': 'Entrada não é um Json Válido'}, 400

    cmd_sql = 'select * from tbl_usuarios WHERE user_id = ?'
    registrado, encontrado = select_query(cmd_sql, user_id)

    if not(encontrado):

        dado = (user_id, content['nome'], content['email'])

        cmd_sql = 'INSERT INTO tbl_usuarios(user_id, nome, email) VALUES (?, ?, ?)'
        sucesso = insert_query(cmd_sql, dado)
        if sucesso:
            return {'Usuário Cadastrado': content}, 201
        else:
            return {'Erro': 'Ocorreu Algum erro ao tentar cadastrar o usuário'}, 500
    else:
        return {'Erro': 'Usuario já existe no cadastro'}, 404


# Operações com a base
@app.route('/usuario/<int:user_id>', methods=['GET'])
def rota_buscar_usuario( user_id ):

    cmd_sql = 'select * from tbl_usuarios WHERE user_id = ?'
    user_data, encontrado = select_query(cmd_sql, user_id)

    resp = {'id':user_data[0], 'nome':user_data[1], 'email':user_data[2]}

    print(resp)
    if encontrado:
        return jsonify(resp), 200
    else:
        return {'Erro': 'Usuário não Encontrado'}, 404


# Operações com a base
@app.route('/usuario', methods=['GET'])
def rota_buscar_todos_usuario():

    cmd_sql = 'select * from tbl_usuarios'
    users, sucesso = select_query(cmd_sql)

    if sucesso:
        return jsonify(users), 200
    else:
        return {'Erro': 'Não foi possivel localizar nenhum usuário'}, 500


# Operações com a base
@app.route('/usuario/<int:user_id>/timeline', methods=['GET'])
def rota_timeline_de_usuario(user_id):

    usuario = User.buscar_usuario_ativo(user_id=user_id)
    time_line = usuario.time_line.to_dict()
    return jsonify(time_line), 200



if __name__ == '__main__':
    app.run(debug=True)