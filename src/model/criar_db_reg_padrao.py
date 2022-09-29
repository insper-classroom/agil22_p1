import sqlite3
from pathlib import Path

# Armazenando referância para raiz do projeto
FILE = Path(__file__).resolve()
src_folder = FILE.parents[0]


def criar_db(caminho_arq_db):

    # Conecta com a base, se não existe cria
    con = sqlite3.connect(caminho_arq_db.resolve())

    # Cria o cursor de conexão com a base
    cur = con.cursor()

    tabela_nome = 'tbl_usuarios'

    # Se a tabela já existe é deletada
    cur.execute(f'DROP TABLE IF EXISTS {tabela_nome}')

    # Cria a tabela zerada
    comando_sql =f'''CREATE TABLE {tabela_nome} (
        "user_id"	INTEGER PRIMARY KEY AUTOINCREMENT,
        "nome"	TEXT,
        "email"	TEXT
    )'''
    # executa o comando sql armazenado na variavel sql
    cur.execute(comando_sql)
    # commita as alterações
    con.commit()

    # fecha a conexão com a base
    con.close()


def load_tabela_registrados(caminho_arq_db):
    # realizando a carga de varios valores na tabela tbl_registrados

    list_of_dicts = []
    list_of_dicts.append((1220, 'Camila', 'camila@email.edu.br'))
    list_of_dicts.append((1221, 'Ramon', 'ramon@email.edu.br'))
    list_of_dicts.append((1222, 'Bruno', 'bruno@email.edu.br'))
    list_of_dicts.append((1223, 'Elisa', 'elisa@email.edu.br'))

    #data = pd.read_csv(caminho_csv.resolve(), encoding="utf-8")
    #list_of_dicts = list(data[['ean', 'name']].dropna().head(2000).itertuples(index=False, name=None))


    con = sqlite3.connect(caminho_arq_db.resolve())

    # https://docs.python.org/2/library/sqlite3.html#sqlite3-controlling-transactions
    # Fill the table
    comando_sql = "INSERT INTO tbl_usuarios(user_id, nome, email) VALUES (?, ?, ?)"
    con.executemany(comando_sql, list_of_dicts)

    # commita as alterações
    con.commit()

    # fecha a conexão com a base
    con.close()


# caminho para a base
rel_arquivo_db = Path('rede_social.db')
caminho_arq_db = src_folder / rel_arquivo_db

# caminho para o arquivo csv
#rel_arquivo_itens = Path('../recursos/itens.csv')
#arquivo_csv = src_folder / rel_arquivo_itens

# Cria a base com uma tabela
criar_db(caminho_arq_db)

# carrega os dados do csv para a tabela
load_tabela_registrados(caminho_arq_db)