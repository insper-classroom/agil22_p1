import pytest
from classes.rede_social import *


@pytest.mark.para_avaliacao
@pytest.mark.post_verificar_adicionar_comentario_repetido
def test_adicionar_comentario_repetido_na_classe_Post():
    pass

@pytest.mark.para_avaliacao
@pytest.mark.post_verificar_remover_comentario
def test_remover_comentario_da_classe_Post():
    pass

@pytest.mark.para_avaliacao
@pytest.mark.comment_verificar_id_proprietario
def test_se_id_proprietario_adicionado_corretamente_na_classe_Comment():
    pass


@pytest.mark.para_avaliacao
@pytest.mark.comment_verificar_conteudo
def test_se_conteudo_adicionado_corretamente_na_classe_Comment():
    pass


@pytest.mark.para_avaliacao
@pytest.mark.comment_verificar_to_dict
def test_se_to_dict_retornado_corretamente_na_classe_Comment():
    pass