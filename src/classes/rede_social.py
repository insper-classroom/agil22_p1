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
        


    @classmethod
    def buscar_usuario_ativo(cls, user_id:int)->User:

        if user_id in cls.dict_usuarios_ativos.keys():
            return cls.dict_usuarios_ativos[user_id]



    def adicionar_amigo(self, amigo:User):

        # verifica se esse amigo já existe na lista antes de adicionar
        if not(amigo in self.amigos):
            self.amigos.append(amigo)
            amigo.amigos.append(self)
            self.qtd_amigos += 1
            amigo.qtd_amigos += 1
            return True
        else:
            return False


    def remover_amigo(self, amigo:User):
    
        # verifica se esse amigo já existe na lista antes de adicionar
        if amigo in self.amigos:
            self.amigos.remove(amigo)
            amigo.amigos.remove(self)
            self.qtd_amigos -= 1
            amigo.qtd_amigos -= 1
            return True
        else:
            return False
            

    # Só comentar se for amigo]
    def comentar_post(self, post:Post, comentario:str):
        if post.proprietario in self.amigos:
            meu_comentario = Comment(self, comentario)
            post.adicionar_comentario(meu_comentario)
            return meu_comentario


    # !!!! Somente o dono do comentario ou dono do post pode remover o comentario
    def remover_comentario_do_post(self, post:Post, comentario:Comment):
        if (comentario != None and (comentario.proprietario_id == self.id or post.proprietario == self) ):
            post.remover_comentario(comentario)


    def escrever_post(self, mensagem:str):
        meu_post = Post(self, mensagem)
        self.time_line.adicionar_post(meu_post)
        return meu_post


    def remover_post_da_timeline(self, post):
        if post in self.time_line.retorna_lista_de_posts():
            self.time_line.remover_post(post)

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

        # Se postagens não estiver zerado, adicionar
        for post in postagens:
            # verifica se é da classe Post
            if type(post) == Post:
                self.__posts.append(post)
                self.__qtd_posts += 1

        # Verifica se existe postagens na base

    def retorna_lista_de_posts(self):
        return self.__posts

    def retorna_qtd_de_posts(self):
        return self.__qtd_posts


    def adicionar_post(self, post):

        if not( post in self.__posts ):
            self.__posts.append(post)
            self.__qtd_posts += 1


    def remover_post(self, post):
    
        if post in self.__posts:
            self.__posts.remove(post)
            self.__qtd_posts -= 1


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