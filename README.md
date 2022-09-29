# prova_agil_2022_2 - # Prova 1

## Projeto Ágil e Programação Eficaz - frente de programação

**Atenção** este projeto de código vale 8.0 pontos. Esta prova é complementada por uma primeira questão feita em papel 

É um pré-requisito para aprovação na disciplina ter tirado mais que $5.0$ em uma prova. 


A média de provas desta parte da disciplina é $MAX(P1, P2)$ de modo que este exame possa ser encarado com tranquilidade. 

## Recomendações gerais 

**Não é permitido** usar Github CoPilot ou recursos equivalentes 

Você pode consultar livremente a internet desde que **não se comunique** com outras pessoas. Nem de dentro nem de fora da sala.

**Feche o WhatsApp** e quaisquer outros recursos de comunicação individual (Outlook, Gmail, etc)

Sua tela será gravada pelo *Proctorio*


## Estrutura do projeto:

Atenção aos arquivos que precisam ser alterados. Você não vai precisar mexer em nenhum outro arquivo. 


```
├── classes_prova.md
├── doc
│   └── diagrama.md
├── pytest.ini
├── requirements.txt
└── src
    ├── app.py  # Alterar para Q3
    ├── classes
    │   ├── __init__.py
    │   └── rede_social.py  # Alterar para Q1
    ├── main.py
    ├── model
    │   ├── __init__.py
    │   ├── criar_db_reg_padrao.py
    │   ├── db.py
    │   └── rede_social.db
    └── test
        ├── __init__.py
        ├── para_postman
        │   └── Prova_Agil_2022_2.postman_collection.json  # Arquivo para Postman e Q3
        ├── test_tdd_prova.py
        └── test_unit_test_prova.py  #Alterar para Q2
```

A questão 1 conta com testes unitários para ajudá-lo a verificar seu progresso. Para executá-los vá à pasta principal do projeto e execute: 

    pytest -v

Recomendamos que use um ambiente virtual para realizar a prova. Se puder deixe-o fora da pasta que contém a prova e não o envie ao Github. 

Existe um *requirements.txt* para comodidade, caso queira usar um *venv.  De qualquer forma não usamos nenhum pacote fora do que foi testado em aula. 

[Questão 1 - classes](./classes_prova.md)


[Home](./README.md)
[Q1](./Q1.md)
[Q2](./Q2.md)
[Q3](./Q3.md)
