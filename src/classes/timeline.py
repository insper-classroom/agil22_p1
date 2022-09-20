from __future__ import annotations
from model.db import *
#from .post import Post

class Timeline:

    def __init__(self, user, postagens=[] ):
        from .post import Post

        self.proprietario = user
        self.__posts = []
        self.__qtd_posts = 0

        # Se postagens não estiver zerado, adicionar
        for post in postagens:
            # verifica se é da classe Post
            if type(post) == Post:
                self.__posts.append(post)
                self.__qtd_posts += 1

        # Verifica se existe postagens na base

    def retorna_lista_de_posts(self, post):
        return self.__posts


    def adicionar_post(self, post):

        if not( post in self.__posts ):
            self.__posts.append(post)
            self.__qtd_posts += 1


    def remover_post(self, post):
    
        if post in self.__posts:
            self.__posts.remove(post)
            self.__qtd_posts -= 1


    def __str__(self):
        # carrega comentario se existir
        s_temp = '\n'
        for p in self.__posts:
            s_temp = s_temp + '*******'
            s_temp = s_temp + str(p)
            s_temp = s_temp + '******* \n'
            

        # continuar na próxima linha
        s = \
        f'''
Timeline do usuario {self.proprietario.nome}
{self.__qtd_posts} posts
Postes:
{s_temp}'''
        return s