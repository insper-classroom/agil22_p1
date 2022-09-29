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


    # Daqui para baixo nesta função o código serve para gerar timeline, que vai ser usada na rota timeline mais abaixo
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
