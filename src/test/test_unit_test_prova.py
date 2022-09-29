import pytest
from classes.rede_social import *

# Você pode querer se inspirar um adaptar um pouco de como os testes foram programados no arquivo test_unit_test.py


@pytest.mark.para_avaliacao
@pytest.mark.post_verificar_adicionar_comentario_repetido
def test_adicionar_comentario_repetido_na_classe_Post():
    """Testa se o método adicionar_comentario() da classe Post permite que se adicionem comentários repetidos
        Um comentário repetido é um comentário com o mesmo conteúdo de outro previamente existente
        Não se deve testar se o objeto é igual
        Deve fazer uma asserção para False se permitir adicionar comentários repetidos
        Mas você não vai precisar corrigir isso
        """
    pass

@pytest.mark.para_avaliacao
@pytest.mark.post_verificar_remover_comentario
def test_remover_comentario_da_classe_Post():
    """Testa se o método remover_comentario() da classe Post permite que se remova um comentário
        Deve fazer uma asserção para True se permitir remover um comentário corretamente
    """
    pass    


@pytest.mark.para_avaliacao
@pytest.mark.comment_verificar_to_dict
def test_se_to_dict_retornado_corretamente_na_classe_Comment():
    """Testa se o método to_dict() da classe Comment retorna um dicionário com as informações corretas
        Inspecione o código de Comment para entender como este método funciona
    """
    pass