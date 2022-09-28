# Prova 1

## Projeto Ágil e Programação Eficaz - frente de programação

**Atenção** este projeto de código vale 8.0 pontos. Esta prova é complementada por uma primeira questão feita em papel 

# Questão sobre modelo de objetos 

Atenção: existem testes unitários no projeto para ajudá-lo a avançar nesta fase. Rode pytest -v na pasta inicial do projeto para ver as dicas. 

## Método para buscar usuários

Adicionar na classe `User` um método chamado `buscar_usuario_ativo` que deve receber como parâmetro um `int` que corresponde ao **id** de um usuário. 

Este método vai ser chamado diretamente na classe, sem que seja preciso criar um objeto para poder chamá-lo. 

O valor de retorno deve ser o usuário, se ele existe na estrutura que guarda usuários ativos.

**Atenção:** Nesta questão não é necessário usar SQL. Vamos buscar objetos da classe `User` que estejam na memória.  Cabe a você identificar como estes usuários já estão guardados. 

## Método para adicionar amigos 

Crie na classe `User` um método chamado `adicionar_amigo` que receberá como parâmetro outro objeto da classe `User` para adicionar como amigo.

Este método deve retornar `True` se o amigo de fato foi adicionado.

Caso o amigo já existisse na lista de amigos, o método deve retornar `False`.

A variável `qtd_amigos` pertencente aos objetos da classe `User` deve ser atualizada adequadamente. 

## Método para remover amigo 

Implemente um método chamado `remover_amigo` que recebe um amigo da classe `User`.

Este amigo passadi deve ser removido da lista de amigos do objeto no qual o método está sendo chamado. 

Ex.: 

```python
    removeu = amigo1.remover_amigo(amigo2)
```

Este método deve retornar `True` se o amigo foi devidamente removido, e caso contrário retornar `False` se o objeto passado não estava entre os amigos. Não se pode remover um amigo que não estava na lista. 


## Método para comentar post 



