import sqlite3


# conn: é a variavel para a conexão com o banco de dados
conn = sqlite3.connect("c:/projetos_sqlite3/BD/meu_banco_de_dados.bd")


# Para operações no banco de dados, você tambem precisara de um cursor,
# que é um objeto que permite executar comandos SQL.
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXIST clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER
    )
''')
