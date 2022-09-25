from pathlib import Path
FILE = Path(__file__).resolve()

if FILE.parents[0].parts[-1] == 'prova_agil_2022_2':
    prj_folder = FILE.parents[0]
elif FILE.parents[0].parts[-2] == 'prova_agil_2022_2':
    prj_folder = FILE.parents[1]

import sys
sys.path.insert(0, prj_folder)

from model.db import *
from classes.rede_social import *
#from src.model.db import *
import pytest




@pytest.mark.tdd_prova_nao_altere_esses_testes
def test_criar_usarios_verificar_dict_de_usuarios_ativos_classe():

    assert len(User.dict_usuarios_ativos) == 0

    usuario_r = User(user_id=1221)
    
    # verifica se usuario foi adicionado  
    assert usuario_r.id in User.dict_usuarios_ativos.keys()
    assert usuario_r == User.dict_usuarios_ativos[usuario_r.id]
    
    usuario_b = User(user_id=1222)
    
    assert usuario_b.id in User.dict_usuarios_ativos.keys()
    assert usuario_r.id in User.dict_usuarios_ativos.keys()
    assert usuario_r == User.dict_usuarios_ativos[usuario_r.id]
    assert usuario_b == User.dict_usuarios_ativos[usuario_b.id]
    
    usuario_e = User(user_id=1223)

    assert len(User.dict_usuarios_ativos) == 3


@pytest.mark.tdd_prova_nao_altere_esses_testes
def test_criar_usarios_verificar_o_objeto_e_atributos_da_classe():

    # verifica usuarios ativos na plataforma
    assert User.usuarios_ativos_na_plataforma == 0

    # cria um usuário que sera buscado na base
    usuario_c = User(user_id=1220)
    
    # cria um usuário sera criado com as infos passadas pelo construtor
    usuario_ed = User(user_id=1, nome='Eduardo', email='eduardo@email.com')

    # verifica usuarios ativos na plataforma
    assert User.usuarios_ativos_na_plataforma == 2

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
    
    # verifica usuarios ativos na plataforma
    assert User.usuarios_ativos_na_plataforma == 5







