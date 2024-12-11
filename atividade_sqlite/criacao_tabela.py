import sqlite3


conn = sqlite3.connect("C:/vinicius/sqlite/atividade_sqlite/aeroporto.db")

cursor = conn.cursor()

# criando as tabelas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS passageiro (
        id_passageiro INTEGER PRIMARY KEY AUTOINCREMENT, 
        nome TEXT NOT NULL,
        CPF INTEGER NOT NULL UNIQUE,  
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
        capacidade INTEGER NOT NULL,
        data_manuntencao DATE NOT NULL
    )
''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS companhia_aerea (
        id_companhia INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_companhia TEXT NOT NULL,
        numero_voo INTEGER NOT NULL,
        avaliacao TEXT
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
        data_voo DATE NOT NULL,
        horario_embarque TIMESTAMP NOT NULL,
        duracao_voo TIMESTAMP NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS ticket (
        ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
        preco REAL NOT NULL,
        data_voo DATE NOT NULL,
        horario_embarque TIMESTAMP NOT NULL,
        duracao_voo TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS pagamento_ticket (
        pagamento_id INTEGER PRIMARY KEY AUTOINCREMENT,
        data_pagamento DATE NOT NULL,
        valor_pago REAL NOT NULL,
        tipo_pagamento TEXT NOT NULL
    )
''')

conn.commit()
conn.close()