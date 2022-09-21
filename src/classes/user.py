from __future__ import annotations
from model.db import *
from .post import Post
#from .timeline import Timeline
from .comment import Comment

class User:

    usuarios_ativos_na_plataforma = 0

    def __init__(self, user_id:int, nome='', email='' ):
        from .timeline import Timeline
    
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

    def __del__(self):
        User.usuarios_ativos_na_plataforma -= 1

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
            

    def alterar_timeline(self, timeline):
        self.time_line = timeline

    
    def escrever_post(self, mensagem:str):
        meu_post = Post(self, mensagem)
        self.time_line.adicionar_post(meu_post)
        return meu_post


    def comentar_post(self, post:Post, comentario:str):
        meu_comentario = Comment(self, comentario)
        post.adicionar_comentario(meu_comentario)
        return meu_comentario


    # !!!! Somente o dono do comentario ou dono do post pode remover o comentario
    def remover_comentario_do_post(self, post:Post, comentario:Comment):
        if (comentario.proprietario_id == self.id or post.proprietario == self ):
            post.remover_comentario(comentario)


    def remover_post_da_timeline(self, post):
        if post in self.time_line.retorna_lista_de_posts:
            self.time_line.remover_post(post)


    #def retornar_posts(self):
    #    return self.time_line.retorna_lista_de_posts()


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


        

