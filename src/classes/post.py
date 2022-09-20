from __future__ import annotations
from model.db import *
from .comment import Comment

class Post:

    def __init__(self, user, conteudo='' ):
        self.proprietario = user
        self.conteudo = conteudo
        self.comentarios = []
        self.qtd_comentarios = 0


    def adicionar_comentario(self, comentario:Comment):
        
        if not(comentario in self.comentarios):
            self.comentarios.append(comentario)
            self.qtd_comentarios +=1


    def remover_comentario(self, comentario:Comment):
        
        if comentario in self.comentarios:
            self.comentarios.remove(comentario)
            self.qtd_comentarios -=1

   
    def __str__(self):
        # carrega comentario se existir
        lista_comentario = []
        for c in self.comentarios:
            lista_comentario.append( str(c) )

        # continuar na próxima linha
        s = \
        f'''
Post do usuario {self.proprietario.nome}
conteudo: {self.conteudo}
{self.qtd_comentarios} comentarios
----
comentarios: {lista_comentario}
----
'''
        return s

