import pytest
import inspect
from classes.rede_social import *
import app


def function_exists_in_module(mod, func):
    if mod == None:
        raise AssertionError('Erro ao carregar solução. Verifique a sintaxe do seu código.')
    all_functions = inspect.getmembers(mod, inspect.isfunction)
    assert any([f[0] == func for f in all_functions]), f'A função {func} não foi definida!'


@pytest.mark.tdd_prova_nao_altere_esses_testes
@pytest.mark.tdd_prova_flask
def test_funcao_inserir_usuario():
    function_exists_in_module(app, 'rota_inserir_usuario')

@pytest.mark.tdd_prova_nao_altere_esses_testes
@pytest.mark.tdd_prova_flask
def test_funcao_buscar_usuario():
    function_exists_in_module(app, "rota_buscar_usuario")

@pytest.mark.tdd_prova_nao_altere_esses_testes
@pytest.mark.tdd_prova_flask
def test_funcao_buscar_todos_usuario():
    function_exists_in_module(app, "rota_buscar_todos_usuario")

@pytest.mark.tdd_prova_nao_altere_esses_testes
@pytest.mark.tdd_prova_flask
def test_funcao_timeline_de_usuario():
    function_exists_in_module(app, "rota_timeline_de_usuario")

