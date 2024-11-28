import sqlite3


# conn: é a variavel para a conexão com o banco de dados
conn = sqlite3.connect("C:/vinicius/sqlite/aula001/arquivo.db")


# Para operações no banco de dados, você tambem precisara de um cursor,
# que é um objeto que permite executar comandos SQL.
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER
    )
''')