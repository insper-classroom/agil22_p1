import sqlite3
from pathlib import Path


# Operações basicas
FILE = Path(__file__).resolve()
src_folder = FILE.parents[0]
rel_arquivo_db = Path('rede_social.db')
db = Path(src_folder / rel_arquivo_db).resolve()


# Utilizado com a operação de SELECT
def select_query(sql, user_id=0):
    sucesso = True
    try:
        # Realiza a conexão com a Base de Dados
        conexao = sqlite3.connect(db)
        cur = conexao.cursor()
        if user_id==0:
            # Executa a query
            cur.execute(sql)
            # Busca todos os registros
            record = cur.fetchall()
        else:
            # Forma segura que passar parâmetro para uma query SQL
            # Evitando SQL Injection, mais infos em https://realpython.com/prevent-python-sql-injection/
            # Executa a query

            cur.execute(sql, (user_id,))
            # Busca apenas um registro
            record = cur.fetchone()
        # Se não encontrou nenhum registro, sucesso é False. 
        # Atenção: Não encontrar registro não gera erro, por isso não irá passar pelo "except"
        if record==None:
            sucesso = False

    except:
        sucesso = False
        record = None
        print(sqlite3.DatabaseError)
    finally:
        # Encerra a conexão
        cur.close();
        conexao.close()
    # Retorna a resposta da Base de Dados
    return record, sucesso


# Utilizado com a operação de INSERT
def insert_query(sql, data):

    # Estamos adicionando essa linha para que após a inserção do registro
    sucesso = True
    try:
        # Realiza a conexão com a Base de Dados
        conexao = sqlite3.connect(db)
        cur = conexao.cursor()
        # Forma segura que passar parâmetro para uma query SQL
        # Evitando SQL Injection, mais infos em https://realpython.com/prevent-python-sql-injection/
        # Executa a query
        cur.execute(sql, data)
        # Realiza o commit da operação
        conexao.commit()
    except:
        sucesso = False
        print(sqlite3.DatabaseError) # Apenas print do erro, tratamento nas próximas aulas
    finally:
        # Encerra a conexão
        cur.close();
        conexao.close()
        
    return sucesso


# Utilizado com a operação de UPDATE
def update_query(sql, data):

    sucesso = True
    try:
        # Realiza a conexão com a Base de Dados
        conexao = sqlite3.connect(db)
        cur = conexao.cursor()
        # Forma segura que passar parâmetro para uma query SQL
        # Evitando SQL Injection, mais infos em https://realpython.com/prevent-python-sql-injection/
        # Executa a query
        cur.execute(sql, data)
        # Qtd de resgistros alterados
        update_rows = cur.rowcount # poderia ser utilizado para verificações
        conexao.commit()
    except:
        update_rows = 0
        sucesso = False
        print(sqlite3.DatabaseError) # Apenas print do erro, tratamento nas próximas aulas
    finally:
        # Encerra a conexão
        cur.close();
        conexao.close()
    return update_rows, sucesso


# Utilizado com a operação de DELETE
def delete_query(sql, user_id):

    sucesso = True
    try:
        # Realiza a conexão com a Base de Dados
        conexao = sqlite3.connect(db)
        cur = conexao.cursor()
        # Forma segura que passar parâmetro para uma query SQL
        # Evitando SQL Injection, mais infos em https://realpython.com/prevent-python-sql-injection/
        # Executa a query
        cur.execute(sql, (user_id,))
        # Qtd de registros deletados
        deleted_rows = cur.rowcount
        # Realiza o commit da operação
        conexao.commit()
    except:
        sucesso = False
        print(sqlite3.DatabaseError) # Apenas print do erro, tratamento nas próximas aulas
    finally:
        # Encerra a conexão
        cur.close();
        conexao.close()
    return deleted_rows, sucesso

