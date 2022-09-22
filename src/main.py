from classes.user import User
from classes.rede_social import User, Timeline, Post, Comment 



# TESTE CRIAÇÃO DE USUARIOS
# =====================================
print(User.usuarios_ativos_na_plataforma)
usuario_c = User(user_id=1220)
usuario_r = User(user_id=1221)
usuario_b = User(user_id=1222)
usuario_e = User(user_id=1223)
usuario_ed = User(user_id=1, nome='Eduardo', email='eduardo@email.com')
print(User.usuarios_ativos_na_plataforma)
#print(usuario_c)
# pensar em verificações simples sobre a contrução do objeto
# Os primeiros quatro vem da base e o Eduardo é criado passando parametros via construtor
# =====================================




# TESTE DE ADICIONAR AMIGOS
# +++++++++++++++++++++++++++++++++++++
usuario_c.adicionar_amigo(usuario_b)
usuario_c.adicionar_amigo(usuario_ed)
usuario_c.adicionar_amigo(usuario_e)

usuario_r.adicionar_amigo(usuario_c)

usuario_b.adicionar_amigo(usuario_e)
usuario_b.adicionar_amigo(usuario_e) # não pode adicionar o mesmo amigo mais de uma vez

# Camila precisa ter 4 amigos (Bruno, Eduardo, Elisa, Ramon)
# Bruno precisa ter 2 amigos (Camila, Elisa)
# Ramon precisa ter 1 amigo (Camila)
# Elisa precisa ter 1 amigo (Bruno)
#print(usuario_c)
#print(usuario_e)
# +++++++++++++++++++++++++++++++++++++



# TESTE TIMELINE
# -------------------------------------
#print(usuario_c.time_line)
#print('\n \n')

post1_c = usuario_c.escrever_post('Meu primeiro Post - Camila')
#print(post1_c)
#print('\n \n')

post2_c = usuario_c.escrever_post('Meu segundo Post - Camila')

#print(usuario_c.time_line)
#print('\n \n')
# Possivel verificar que as duas postagens estão na timeline da Camila
# Inicialmente sem comentario nenhum

comentario_r_para_c_post_1 = usuario_r.comentar_post(post1_c, 'Comentario de Ramon no Post 1 de Camila')
comentario_r_para_c_post_2 = usuario_r.comentar_post(post2_c, 'Comentario de Ramon no Post 2 de Camila')
comentario_e_para_c_post_2 = usuario_e.comentar_post(post2_c, 'Comentario de Eliza no Post 2 de Camila')
#print(comentario_e_para_c_post_2) # verifica comentario
#print('\n')
#print(post2_c) # verifica se adicionado no post
#print('\n')
#print(usuario_c.time_line) # verifica na Timeline
#print('\n \n')


post1_b = usuario_b.escrever_post('Meu primeiro Post - Bruno')
comentario_ed_para_b_post_2 = usuario_ed.comentar_post(post1_b, 'Comentario de Eduardo no Post 1 de Bruno')
comentario_ed_para_b_post_2_repetido = usuario_ed.comentar_post(post1_b, 'Comentario de Eduardo no Post 1 de Bruno - REPETIDO')
comentario_r_para_b_post_2 = usuario_r.comentar_post(post1_b, 'Comentario de Ramon no Post 1 de Bruno')
#print(usuario_b.time_line) # verifica na Timeline
#print('\n \n')


# camila vai tentar remover e o post deve continuar
usuario_c.remover_comentario_do_post(post1_b, comentario_ed_para_b_post_2_repetido)
#print(usuario_b.time_line) # verifica na Timeline

# agora o dono do comentario irá remover
usuario_ed.remover_comentario_do_post(post1_b, comentario_ed_para_b_post_2_repetido)
#print(usuario_b.time_line)

# Comentario de Ramon será removido pelo proprio Bruno
usuario_b.remover_comentario_do_post(post1_b, comentario_r_para_b_post_2)
#print(usuario_b.time_line)
#--------------------------------------



# REMOVER AMIGOS DA CAMILA
# +++++++++++++++++++++++++++++++++++++
# remover um que não existe e depois um que existe na lista, ela mesma
print(usuario_c)
print('\n \n')
usuario_c.remover_amigo(usuario_c)
print(usuario_c)
print('\n \n')
usuario_c.remover_amigo(usuario_r)
print(usuario_c)
print(usuario_r)
# +++++++++++++++++++++++++++++++++++++