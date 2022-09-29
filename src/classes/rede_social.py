from __future__ import annotations
from model.db import *


class User:
    
    usuarios_ativos_na_plataforma = 0
    dict_usuarios_ativos = {}

    def __init__(self, user_id:int, nome='', email='' ):
        
        # obrigatório email e senha para criação do usuário
        if (nome=='' and email==''):
            # verificando se usuário já existe na base
            cmd_sql = 'select * from tbl_usuarios WHERE user_id = ?'
            user_data, encontrado = select_query(cmd_sql, user_id)
            if encontrado:
                self.id = user_id
                self.nome = user_data[1]
                self.email = user_data[2]
            else:
                raise ('Usuário não encontrado na base.')
        elif (nome!='' and email!=''):
            self.id = user_id
            self.nome = nome
            self.email = email
        else:
            raise ('Atributos nome e email não encontrado para criação do objeto.')

        self.amigos = []
        self.time_line = Timeline(self)
        self.qtd_amigos = 0
        User.usuarios_ativos_na_plataforma += 1
        User.dict_usuarios_ativos[user_id] = self


    def __del__(self):
        User.dict_usuarios_ativos.pop(self.id, None)
        User.usuarios_ativos_na_plataforma -= 1
        



    def __str__(self):

        s_temp = '\n'
        for amigo in self.amigos:
            s_temp = s_temp + f'  {amigo.id} - {amigo.nome} \n'
        s_temp = s_temp + '\n'


        # continuar na próxima linha
        s = \
        f'''
Usuario {self.nome}
Tem {self.qtd_amigos} amigos
Amigos:
{s_temp}

Timeline:
{self.time_line}
    
        '''
        return s




class Comment:
    
    def __init__(self, user:User, comentario:str):
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

    def to_dict(self):
        return {'user_id':self.proprietario_id, 'comentario':self.__conteudo}

    def __str__(self):
        return f'{self.proprietario_id}: {self.__conteudo}'




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

    def to_dict(self):
        temp_post = {}
        temp_post['conteudo'] = self.conteudo
        temp_post['qtd_comentarios'] = self.qtd_comentarios

        temp_post['comentarios'] = []
        for comentario in self.comentarios:
            temp_post['comentarios'].append( comentario.to_dict() )

        return temp_post

   
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




class Timeline:
    
    def __init__(self, user, postagens=[] ):
        #from .post import Post

        self.proprietario = user
        self.__posts = []
        self.__qtd_posts = 0

    def retorna_lista_de_posts(self):
        return self.__posts

    def retorna_qtd_de_posts(self):
        return self.__qtd_posts


    def to_dict(self):

        timeline = {}
        timeline['qtd_posts'] = self.__qtd_posts
        user_posts = []
        for post in self.__posts:
            user_posts.append(post.to_dict()) 
        timeline['posts'] = user_posts

        dict_obj = {}
        dict_obj['user_id'] = self.proprietario.id
        dict_obj['nome'] = self.proprietario.nome
        dict_obj['timeline']= timeline

        return dict_obj


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
