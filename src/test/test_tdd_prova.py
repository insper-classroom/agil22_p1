import pytest
from classes.rede_social import *


@pytest.mark.tdd_prova_nao_altere_esses_testes
def test_criar_usarios_verificar_dict_de_usuarios_ativos_classe():

    assert len(User.dict_usuarios_ativos) == 0

    usuario_r = User(user_id=1221)
    
    # verifica se usuario foi adicionado  
    assert usuario_r.id in User.dict_usuarios_ativos.keys()
    assert usuario_r == User.dict_usuarios_ativos[usuario_r.id]
    
    usuario_b = User(user_id=1222)

    # verifica usuarios ativos na plataforma
    assert User.usuarios_ativos_na_plataforma == 2
    
    assert usuario_b.id in User.dict_usuarios_ativos.keys()
    assert usuario_r.id in User.dict_usuarios_ativos.keys()
    assert usuario_r == User.dict_usuarios_ativos[usuario_r.id]
    assert usuario_b == User.dict_usuarios_ativos[usuario_b.id]
    
    usuario_e = User(user_id=1223)

    assert len(User.dict_usuarios_ativos) == 3


@pytest.mark.tdd_prova_nao_altere_esses_testes
def test_criar_usarios_verificar_o_objeto_e_atributos_da_classe():

    # cria um usuário que sera buscado na base
    usuario_c = User(user_id=1220)
    
    # cria um usuário sera criado com as infos passadas pelo construtor
    usuario_ed = User(user_id=1, nome='Eduardo', email='eduardo@email.com')


    # Verifica os atributos do objeto do usuario Camila, puxado da base
    assert usuario_c.nome == 'Camila'
    assert usuario_c.email == 'camila@email.edu.br'
    assert usuario_c.nome != 'Eduardo' # verifica se não foi sobrescrito informação do objeto do usuario Camila

    # Verifica usuario criado sem a base
    assert usuario_ed.nome == 'Eduardo'
    assert usuario_ed.email == 'eduardo@email.com'

    usuario_r = User(user_id=1221)
    usuario_b = User(user_id=1222)
    usuario_e = User(user_id=1223)


@pytest.mark.tdd_prova_nao_altere_esses_testes
def test_adicionar_amigos():

    usuario_c = User(user_id=1220)
    usuario_r = User(user_id=1221)
    usuario_b = User(user_id=1222)
    usuario_e = User(user_id=1223)
    usuario_ed = User(user_id=1, nome='Eduardo', email='eduardo@email.com')

    # Ao adicionar um amigo o usuario também deve ser adicionado na lista de amigos desse amigo
    usuario_c.adicionar_amigo(usuario_b)
    usuario_c.adicionar_amigo(usuario_ed)
    usuario_c.adicionar_amigo(usuario_e)
    usuario_r.adicionar_amigo(usuario_c)
    # teste de duplicidade
    usuario_b.adicionar_amigo(usuario_e)
    usuario_b.adicionar_amigo(usuario_e)

    # verificando amigos de camila
    assert usuario_b in usuario_c.amigos
    assert usuario_r in usuario_c.amigos
    assert usuario_e in usuario_c.amigos
    assert usuario_ed in usuario_c.amigos
    assert not(usuario_c in usuario_c.amigos)
    assert usuario_c.qtd_amigos == 4

    # verificando amigos de Bruno
    assert usuario_c in usuario_b.amigos
    assert not(usuario_r in usuario_b.amigos)
    assert usuario_e in usuario_b.amigos
    assert not(usuario_ed in usuario_b.amigos)
    assert not(usuario_r in usuario_b.amigos)
    assert usuario_b.qtd_amigos == 2

    # verificando Elisa
    assert usuario_b in usuario_e.amigos
    assert usuario_c in usuario_e.amigos
    assert not(usuario_r in usuario_e.amigos)
    assert usuario_e.qtd_amigos == 2


@pytest.mark.tdd_prova_nao_altere_esses_testes
def test_remover_amigos():

    usuario_c = User(user_id=1220)
    usuario_r = User(user_id=1221)
    usuario_b = User(user_id=1222)
    usuario_e = User(user_id=1223)
    usuario_ed = User(user_id=1, nome='Eduardo', email='eduardo@email.com')

    # Ao adicionar um amigo o usuario também deve ser adicionado na lista de amigos desse amigo
    usuario_c.adicionar_amigo(usuario_b)
    usuario_c.adicionar_amigo(usuario_ed)
    usuario_c.adicionar_amigo(usuario_e)
    usuario_r.adicionar_amigo(usuario_c)
    usuario_b.adicionar_amigo(usuario_e)

    # usuario Camila
    assert usuario_c.qtd_amigos == 4
    usuario_c.remover_amigo(usuario_b)
    assert usuario_c.qtd_amigos == 3
    assert not(usuario_b in usuario_c.amigos)
    assert usuario_b.qtd_amigos == 1
    assert not(usuario_c in usuario_b.amigos)
    
    # não deve remover novamente e nem resultar em bug
    usuario_c.remover_amigo(usuario_b)
    assert usuario_c.qtd_amigos == 3


    usuario_e.remover_amigo(usuario_b)
    assert usuario_b.qtd_amigos == 0
    assert usuario_e.qtd_amigos == 1
    assert not(usuario_b in usuario_e.amigos)
    assert not(usuario_e in usuario_b.amigos)


@pytest.mark.tdd_prova_nao_altere_esses_testes
def test_adicionar_post_na_timeline():

    usuario_c = User(user_id=1220)
    usuario_r = User(user_id=1221)
    usuario_b = User(user_id=1222)
    usuario_e = User(user_id=1223)
    usuario_ed = User(user_id=1, nome='Eduardo', email='eduardo@email.com')

    usuario_c.adicionar_amigo(usuario_b)
    usuario_c.adicionar_amigo(usuario_ed)
    usuario_c.adicionar_amigo(usuario_e)
    usuario_r.adicionar_amigo(usuario_c)
    usuario_b.adicionar_amigo(usuario_e)


    assert 0 == usuario_c.time_line.retorna_qtd_de_posts()
    post1_c = usuario_c.escrever_post('Meu primeiro Post - Camila')
    assert 1 == usuario_c.time_line.retorna_qtd_de_posts()
    post2_c = usuario_c.escrever_post('Meu segundo Post - Camila')
    assert 2 == usuario_c.time_line.retorna_qtd_de_posts()


    assert post1_c in usuario_c.time_line.retorna_lista_de_posts()
    assert post2_c in usuario_c.time_line.retorna_lista_de_posts()

    assert post1_c.proprietario == usuario_c
    assert post1_c.conteudo == 'Meu primeiro Post - Camila'
    assert post1_c.conteudo != 'Meu segundo Post - Camila'
    assert not(post1_c.proprietario == usuario_b)

    post1_r = usuario_r.escrever_post('Meu primeiro Post - Ramon')
    assert not(post1_r in usuario_c.time_line.retorna_lista_de_posts())
    assert post1_r in usuario_r.time_line.retorna_lista_de_posts()
    assert 1 == usuario_r.time_line.retorna_qtd_de_posts()


@pytest.mark.tdd_prova_nao_altere_esses_testes
def test_remover_post_da_timeline():

    usuario_c = User(user_id=1220)
    usuario_r = User(user_id=1221)
    usuario_b = User(user_id=1222)
    usuario_e = User(user_id=1223)
    usuario_ed = User(user_id=1, nome='Eduardo', email='eduardo@email.com')

    usuario_c.adicionar_amigo(usuario_b)
    usuario_c.adicionar_amigo(usuario_ed)
    usuario_c.adicionar_amigo(usuario_e)
    usuario_r.adicionar_amigo(usuario_c)
    usuario_b.adicionar_amigo(usuario_e)


    post1_c = usuario_c.escrever_post('Meu primeiro Post - Camila')
    post2_c = usuario_c.escrever_post('Meu segundo Post - Camila')
    post1_r = usuario_r.escrever_post('Meu primeiro Post - Ramon')

    assert 2 == usuario_c.time_line.retorna_qtd_de_posts()
    assert 1 == usuario_r.time_line.retorna_qtd_de_posts()

    # só pode remover seus posts da time line
    usuario_r.remover_post_da_timeline(post1_c)
    usuario_r.remover_post_da_timeline(post2_c)

    assert 2 == usuario_c.time_line.retorna_qtd_de_posts()
    assert 1 == usuario_r.time_line.retorna_qtd_de_posts()

    usuario_c.remover_post_da_timeline(post2_c)
    usuario_r.remover_post_da_timeline(post1_r)

    assert 1 == usuario_c.time_line.retorna_qtd_de_posts()
    assert 0 == usuario_r.time_line.retorna_qtd_de_posts()

    assert post1_c in usuario_c.time_line.retorna_lista_de_posts()
    assert not(post2_c in usuario_c.time_line.retorna_lista_de_posts())
    assert not(post1_r in usuario_r.time_line.retorna_lista_de_posts())



@pytest.mark.tdd_prova_nao_altere_esses_testes
def test_comentar_post_de_um_amigo():

    usuario_c = User(user_id=1220)
    usuario_r = User(user_id=1221)
    usuario_b = User(user_id=1222)
    usuario_e = User(user_id=1223)
    usuario_ed = User(user_id=1, nome='Eduardo', email='eduardo@email.com')

    usuario_c.adicionar_amigo(usuario_b)
    usuario_c.adicionar_amigo(usuario_ed)
    usuario_c.adicionar_amigo(usuario_e)
    usuario_r.adicionar_amigo(usuario_c)
    usuario_b.adicionar_amigo(usuario_e)
    usuario_ed.adicionar_amigo(usuario_b)


    post1_c = usuario_c.escrever_post('Meu primeiro Post - Camila')
    post2_c = usuario_c.escrever_post('Meu segundo Post - Camila')
    post1_r = usuario_r.escrever_post('Meu primeiro Post - Ramon')

    assert post2_c.qtd_comentarios == 0

    comentario_r_para_c_post_1 = usuario_r.comentar_post(post1_c, 'Comentario de Ramon no Post 1 de Camila')
    comentario_r_para_c_post_2 = usuario_r.comentar_post(post2_c, 'Comentario de Ramon no Post 2 de Camila')
    comentario_e_para_c_post_2 = usuario_e.comentar_post(post2_c, 'Comentario de Eliza no Post 2 de Camila')

    assert post2_c.qtd_comentarios == 2
    assert comentario_r_para_c_post_1 in post1_c.comentarios
    assert comentario_r_para_c_post_2 in post2_c.comentarios
    assert comentario_e_para_c_post_2 in post2_c.comentarios


    post1_b = usuario_b.escrever_post('Meu primeiro Post - Bruno')
    comentario_ed_para_b_post_2 = usuario_ed.comentar_post(post1_b, 'Comentario de Eduardo no Post 1 de Bruno')
    comentario_ed_para_b_post_2_repetido = usuario_ed.comentar_post(post1_b, 'Comentario de Eduardo no Post 1 de Bruno - REPETIDO')
    # Não é amigo, não deve comentar
    comentario_r_para_b_post_2 = usuario_r.comentar_post(post1_b, 'Comentario de Ramon no Post 1 de Bruno')
    assert comentario_r_para_b_post_2 == None

    assert post1_b.qtd_comentarios == 2
    assert comentario_r_para_c_post_2.conteudo == 'Comentario de Ramon no Post 2 de Camila'
    assert comentario_r_para_c_post_2.proprietario_id == usuario_r.id
    assert comentario_ed_para_b_post_2.proprietario_id == usuario_ed.id

    assert not(comentario_ed_para_b_post_2 in post2_c.comentarios)
    assert comentario_ed_para_b_post_2_repetido in post1_b.comentarios
    assert comentario_ed_para_b_post_2 in post1_b.comentarios

    



@pytest.mark.tdd_prova_nao_altere_esses_testes
def test_remover_comentario_de_post():
    # Somente o dono do comentario ou dono do post podem remover o comentario

    usuario_c = User(user_id=1220)
    usuario_r = User(user_id=1221)
    usuario_b = User(user_id=1222)
    usuario_e = User(user_id=1223)
    usuario_ed = User(user_id=1, nome='Eduardo', email='eduardo@email.com')

    usuario_c.adicionar_amigo(usuario_b)
    usuario_c.adicionar_amigo(usuario_ed)
    usuario_c.adicionar_amigo(usuario_e)
    usuario_r.adicionar_amigo(usuario_c)
    usuario_b.adicionar_amigo(usuario_e)
    usuario_ed.adicionar_amigo(usuario_b)


    post1_c = usuario_c.escrever_post('Meu primeiro Post - Camila')
    post2_c = usuario_c.escrever_post('Meu segundo Post - Camila')
    post1_r = usuario_r.escrever_post('Meu primeiro Post - Ramon')

    comentario_r_para_c_post_1 = usuario_r.comentar_post(post1_c, 'Comentario de Ramon no Post 1 de Camila')
    comentario_r_para_c_post_2 = usuario_r.comentar_post(post2_c, 'Comentario de Ramon no Post 2 de Camila')
    comentario_e_para_c_post_2 = usuario_e.comentar_post(post2_c, 'Comentario de Eliza no Post 2 de Camila')

    post1_b = usuario_b.escrever_post('Meu primeiro Post - Bruno')
    comentario_ed_para_b_post_2 = usuario_ed.comentar_post(post1_b, 'Comentario de Eduardo no Post 1 de Bruno')
    comentario_ed_para_b_post_2_repetido = usuario_ed.comentar_post(post1_b, 'Comentario de Eduardo no Post 1 de Bruno - REPETIDO')
    comentario_r_para_b_post_2 = usuario_r.comentar_post(post1_b, 'Comentario de Ramon no Post 1 de Bruno')

    # camila vai tentar remover e o post deve continuar
    usuario_c.remover_comentario_do_post(post1_b, comentario_ed_para_b_post_2_repetido)
    assert comentario_ed_para_b_post_2_repetido in post1_b.comentarios
    assert comentario_ed_para_b_post_2 in post1_b.comentarios

    # agora o dono do comentario irá remover
    usuario_ed.remover_comentario_do_post(post1_b, comentario_ed_para_b_post_2_repetido)
    assert not(comentario_ed_para_b_post_2_repetido in post1_b.comentarios)

    # Comentario de Ramon será removido pelo proprio Bruno
    usuario_b.remover_comentario_do_post(post1_b, comentario_r_para_b_post_2)
    assert not(comentario_r_para_b_post_2 in post1_b.comentarios)
    assert post1_b.qtd_comentarios == 1
