import sqlite3


conn = sqlite3.connect("C:/vinicius/sqlite/atividade_sqlite/aeroporto.db")
conn.execute("PRAGMA foreign_keys = ON;") # ativar o ON DELETE/UPDATE CASCADE
cursor = conn.cursor()

# criando as tabelas

cursor.execute('''
    CREATE TABLE IF NOT EXISTS passageiro (
        id_passageiro INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        CPF CHAR(11) NOT NULL UNIQUE,  
        data_de_nascimento DATE NOT NULL,  
        classe TEXT NOT NULL,
        assento TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS terminal_viagens (
        id_terminal INTEGER PRIMARY KEY AUTOINCREMENT,  
        status_voo TEXT NOT NULL,
        horario_embarque TIMESTAMP NOT NULL,  
        destino TEXT NOT NULL,  
        portao INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS aviao (
        id_aviao INTEGER PRIMARY KEY AUTOINCREMENT,  
        modelo TEXT NOT NULL,
        capacidade INTEGER NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS companhia_aerea (
        id_companhia INTEGER PRIMARY KEY AUTOINCREMENT,
        id_aviao INTEGER,
        nome_companhia TEXT NOT NULL,
        numero_voo INTEGER NOT NULL,
        FOREIGN KEY (id_aviao) REFERENCES aviao(id_aviao) ON DELETE CASCADE ON UPDATE CASCADE 
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS rota (
        id_rota INTEGER PRIMARY KEY AUTOINCREMENT,
        origem TEXT NOT NULL,
        destino TEXT NOT NULL,
        UNIQUE (origem, destino)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS voo (
        id_voo INTEGER PRIMARY KEY AUTOINCREMENT,
        id_companhia INTEGER,
        data_voo DATE NOT NULL,
        horario_embarque TIMESTAMP NOT NULL,
        FOREIGN KEY (id_companhia) REFERENCES companhia_aerea(id_companhia) ON DELETE CASCADE ON UPDATE CASCADE 
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS ticket (
        ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
        preco REAL NOT NULL,
        id_rota INTEGER,
        data_voo DATE NOT NULL,
        horario_embarque TIMESTAMP NOT NULL,
        duracao_voo TEXT NOT NULL,
        id_passageiro INTEGER,
        id_terminal INTEGER,  
        FOREIGN KEY (id_rota) REFERENCES rota(id_rota) ON DELETE CASCADE,
        FOREIGN KEY (id_passageiro) REFERENCES passageiro(id_passageiro) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (id_terminal) REFERENCES terminal_viagens(id_terminal) ON DELETE CASCADE ON UPDATE CASCADE 
    )
''')

cursor.execute('''
        CREATE TABLE IF NOT EXISTS pagamento (
        pagamento_id INTEGER PRIMARY KEY AUTOINCREMENT,
        ticket_id INTEGER,
        id_passageiro INTEGER,
        data_pagamento DATE NOT NULL,
        valor_pago REAL NOT NULL,
        FOREIGN KEY (ticket_id) REFERENCES ticket(ticket_id) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (id_passageiro) REFERENCES passageiro(id_passageiro) ON DELETE CASCADE ON UPDATE CASCADE
    )
''')

conn.commit()
conn.close()