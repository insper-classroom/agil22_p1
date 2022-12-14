# Prova 1 - 2022

## Projeto Ágil e Programação Eficaz - frente de programação

**Atenção** este projeto de código vale 8.0 pontos. Esta prova é complementada por uma primeira questão feita em papel 

É um pré-requisito para aprovação na disciplina ter tirado mais que $5.0$ em uma prova. 


A média de provas desta parte da disciplina é $MAX(P1, P2)$ de modo que este exame possa ser encarado com tranquilidade. 

## Recomendações gerais 

**Não é permitido** usar Github CoPilot ou recursos equivalentes 

Você pode consultar livremente a internet desde que **não se comunique** com outras pessoas. Nem de dentro nem de fora da sala.

**Feche o WhatsApp** e quaisquer outros recursos de comunicação individual (Outlook, Gmail, etc)

Sua tela será gravada pelo *Proctorio*, então não esqueça de manter a aba do Blackboard aberta, mesmo que em segundo plano, durante o periodo da prova

O envio é pelo repositório do Github Classroom. Faça envios frequentes (add + commit + push)

**Desligue o celular**

[**Dúvidas** deverão ser tiradas via planilha, com uma descrição clara e suficiente para a sua completa compreensão: Planilha de Dúvidas](https://docs.google.com/spreadsheets/d/1_coT1y0jJQLcq-36JvT5sBIhJRb8q8xEPj1BbOvDJA4/edit#gid=0)


## Estrutura do projeto:

Atenção aos arquivos que precisam ser alterados. Você não vai precisar mexer em nenhum outro arquivo. 


```
├── Q1.md
├── Q2.md
├── Q3.md
├── README.md
├── classes_prova.md
├── doc
│   ├── diagrama.md
│   └── postman_ex_resposta_esperada.png
├── pytest.ini
├── requirements.txt
└── src
    ├── app.py **Usada na Q3
    ├── classes
    │   ├── __init__.py
    │   └── rede_social.py ** Usada na Q1
    ├── main.py
    ├── model
    │   ├── __init__.py
    │   ├── criar_db_reg_padrao.py
    │   ├── db.py
    │   └── rede_social.db
    └── test
        ├── __init__.py
        ├── para_postman
        │   └── Prova_Agil_2022_2.postman_collection.json **Usar no Postman na Q3
        ├── test_tdd_prova.py
        └── test_unit_test_prova.py  **Alterar para Q2
```

A questão 1 conta com testes unitários para ajudá-lo a verificar seu progresso. Para executá-los vá à pasta principal do projeto e execute: 

    pytest -v -m tdd_prova_nao_altere_esses_testes

Recomendamos que use um ambiente virtual para realizar a prova. Se puder deixe-o fora da pasta que contém a prova e não o envie ao Github. 

Existe um *requirements.txt* para comodidade, caso queira usar um *venv.  De qualquer forma não usamos nenhum pacote fora do que foi testado em aula. 

[Questão 1 - classes](./classes_prova.md)


[Home](./README.md)
[Q1](./Q1.md)
[Q2](./Q2.md)
[Q3](./Q3.md)
