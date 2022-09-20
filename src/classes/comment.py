from __future__ import annotations
from model.db import *



class Comment:

    def __init__(self, user, comentario:str):
        # Não iremos carregar o objeto para não sobrecarregar o desenvolvimento ao ter que ler
        # os valores da base para construir o objeto User para atrelar aos comentarios de um post
        self.proprietario_id = user.id
        self.__conteudo = comentario

    @property
    def conteudo(self):
        return self.__conteudo

    @conteudo.setter
    def conteudo(self, novo_conteudo):
        self.__conteudo = novo_conteudo

    def __str__(self):
        return f'{self.proprietario_id}: {self.__conteudo}' 