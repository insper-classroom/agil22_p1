# Classes usadas nas Questões

```mermaid

classDiagram
class User {
+ind: int
+nome: str
+email: str
+amigo:list~User
+qtd_amigos: int
+time_line: ~Timeline
+<< static >> usuarios_ativos_na_plataforma: int
+<< static >> dict_usuarios_ativos: list~User~
+adicionar_amigo(amigo:~User~): bool
+remover_amigo(amigo:~User~): bool
+escrever_post(mensagem:str):~Post~
+remover_post_da_timeline(post:~Post~)
+comentar_post(post:~Post~, comentario:str):~Comment~
+remover_comentario_do_post(post:~Post~, comentario:~Comment~)
classmethod +buscar_usuario_ativo(user_id:int):~User~
+__str__()
}
class Timeline {
+proprietario: User
-posts: list~Post~
-qtd_posts: int 
+retorna_lista_de_posts():list~Post~
+adicionar_post(post:~Post~)
+remover_post(post:~Post~)
+to_dict(): dict
+__str__()
}
class Post {
+proprietario: User
+conteudo: str
+comentarios:list~Comment~
+qtd_comentarios:int
+adicionar_comentario(comentario:~Comment~)
+remover_comentario(comentario:~Comment~)
+to_dict(): dict
+__str__()
}
class Comment {
+proprietario_id: int
-conteudo: str
+to_dict(): dict
+__str__()
}
User "1" -- "1" Timeline : Tem
Timeline "1" o-- "n" Post
Post "1" o-- "n" Comment : Tem
User "1" .. "n" Post : Escreve post
User "1" ..> "n" Comment : Comenta post
User "n" ..o "m" User : É amigo de 


```

## Explicação 

Tratam-se de objetos para uma rede social simples. Estas classes estão detalhadas no arquivo rede_social.py. 

Basicamente cada `User` tem uma `Timeline` em que vai publicando objetos do tipo `Post`

Um `User` adiciona outros como amigos. Um usuário pode ter de $0$ a $n$ amigos. 

Os *posts* podem receber comentários do próprio `User` ou de seus amigos. 

O próprio `User` ou seus amigos podem fazer comentários em seus posts. O arquivo de testes  ``src/test/test_tdd_prova.py` tem alguns exemplos de uso dos objetos deste modelo. 
