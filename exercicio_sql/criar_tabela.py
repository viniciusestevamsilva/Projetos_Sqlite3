import sqlite3


conn = sqlite3.connect("C:/vinicius/sqlite/exercicio_sql/viagens.db")
conn.execute("PRAGMA foreign_keys = ON;")
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS passageiro (
        id_passageiro INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        CPF CHAR(11) NOT NULL UNIQUE,  
        data_nascimento DATE NOT NULL,  
        origem_viagem TEXT NOT NULL,
        destino_viagem TEXT NOT NULL
        )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS minha_passagens (
        id_passagem INTEGER PRIMARY KEY AUTOINCREMENT,
        id_passageiro INTEGER,
        preco REAL NOT NULL,
        duracao_viagem TIMESTAMP,
        data_viagem DATE,
        origem_destino TEXT,
        FOREIGN KEY (id_passageiro) REFERENCES passageiro(id_passageiro) ON DELETE CASCADE ON UPDATE CASCADE
        FOREIGN KEY (origem_destino) REFERENCES voos(origem_destino) ON DELETE CASCADE ON UPDATE CASCADE
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS voos (
        origem_destino TEXT PRIMARY KEY,
        status_voo TEXT NOT NULL,
        passagens_disponiveis INTEGER NOT NULL,
        preco_passagem REAL NOT NULL,
        companhia_responsavel TEXT,
        FOREIGN KEY (companhia_responsavel) REFERENCES companhias(nome_companhia) ON DELETE CASCADE ON UPDATE CASCADE
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS companhias(
        nome_companhia TEXT PRIMARY KEY,
        numero_voo INTEGER NOT NULL,
        avaliacao INTEGER NOT NULL,
        aviao TEXT NOT NULL,
        capacidade INTEGER NOT NULL
        )
''')

conn.commit()
conn.close()

print("|------------------------------------|")
print("|    Tabelas criadas com sucesso !   |")
print("|------------------------------------|")