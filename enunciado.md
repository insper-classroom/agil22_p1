# Prova 1

## Projeto Ágil e Programação Eficaz - frente de programação

**Atenção** este projeto de código vale 8.0 pontos. Esta prova é complementada por uma primeira questão feita em papel 

# Questão sobre modelo de objetos 

Atenção: existem testes unitários no projeto para ajudá-lo a avançar nesta fase. Rode pytest -v na pasta inicial do projeto para ver as dicas. 

Você pode ler os testes do arquivo `src/test/test_tdd_prova.py` para entender como os objetos funcionam. Mas não é esperado que você edite este arquivo. 


## Método para buscar usuários

Adicionar na classe `User` um método chamado `buscar_usuario_ativo` que deve receber como parâmetro um `int` que corresponde ao **id** de um usuário. 

**Atenção:** este é o único método desta questão que recebe um **id** inteiro em vez de um objeto. 

Este método vai ser chamado diretamente na classe, sem que seja preciso criar um objeto para poder chamá-lo. 

O valor de retorno deve ser o usuário, se ele existe na estrutura que guarda usuários ativos.

**Atenção:** Nesta questão não é necessário usar SQL. Vamos buscar objetos da classe `User` que estejam na memória.  Cabe a você identificar como estes usuários já estão guardados. 

## Método para adicionar amigos 

Crie na classe `User` um método chamado `adicionar_amigo` que receberá como parâmetro outro objeto `amigo2` da classe `User` para adicionar como amigo.

Este método deve retornar `True` se o `amigo2` de fato foi adicionado.  

Caso o `amigo2` já existisse previamente na lista de amigos, o método deve retornar `False`.

A variável `qtd_amigos` pertencente aos objetos da classe `User` deve ser atualizada adequadamente tanto no próprio objeto quanto no objeto `amigo2` recebido. 

O próprio objeto da classe `User` - o `self` - precisa também se adicionar como amigo no `amigo2`. 



## Método para remover amigo 

Implemente um método chamado `remover_amigo` que recebe um objeto `amigo2` da classe `User`.

Este amigo passado deve ser removido da lista de amigos do objeto atual.  A variável `qtd_amigos` deve ser ajustada corretamente tanto no `self` quanto no objeto passado.  


Exemplo de uso. Note que você vai programar num contexto em que `amigo1` será o `self`.: 

```python
    removeu = amigo1.remover_amigo(amigo2)
```

Este método deve retornar `True` se o amigo foi devidamente removido, e caso contrário retornar `False` se o objeto passado não estava entre os amigos. Não se pode remover um amigo que não estava na lista. 

O objeto da classe `User` deve também se remover do `amigo2`. 

## Método para escrever post e adicionar à *timeline*

Crie um método chamado `escrever_post` na classe `User`.  

O método deve receber uma `str` com o conteúdo do post e usá-lo para instanciar um objeto da classe `Post` e adicioná-lo à *timeline* do objeto da classe `User`. 

Para facilidade de testes no futuro, além de adicionar na *timeline* este método retorna o objeto `Post` que foi criado. 

## Método para remover post da timeline 

Este método deve pertencer à classe `User`. Recebe um *post* e o remove da *timeline*. 

Deve-se validar se o `Post` está mesmo na *timeline*.

## Método para comentar post 

Crie um método na classe `User` que: 

* Recebe um objeto `Post` já criado. Este `Post` pode pertencer a outro `User`
* Recebe uma `str` com uma mensagem
* Cria um objeto da classe `Comment` contendo a mensagem
* Adiciona o novo `Comment` como comentário ao `Post`

Devolve o objeto `Comment` criado

Atenção: só se pode comentar um `Post` se ele for de um amigo do `User`. 

## Método para remover comentário do post 

Este método recebe um objeto `Post` e um objeto `Comment`.  

O `Comment` deve ser removido do `Post`

Uma regra que deve ser seguida é que somente o autor do Post ou o autor do comentário Comment podem excluir comentário. 


# Questão sobre testes unitários 

# Questão sobre Flask 


