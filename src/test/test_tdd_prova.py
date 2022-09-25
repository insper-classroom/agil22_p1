import pytest

#from model.db import *
from classes.rede_social import *
#from src.model.db import *




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







