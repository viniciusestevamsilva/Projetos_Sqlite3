import sqlite3

conn = sqlite3.connect("C:/vinicius/sqlite/projeto_sqlite/aeroporto.db")

cursor = conn.cursor()


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
    CREATE TABLE IF NOT EXISTS companhia_aerea (
        id_companhia INTEGER PRIMARY KEY AUTOINCREMENT,  
        nome_companhia TEXT NOT NULL,
        numero_voo INTEGER NOT NULL,  
        id_aviao INTEGER NOT NULL  
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS ticket (
        ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,  
        preco REAL NOT NULL,  
        origem_destino TEXT NOT NULL,
        data_voo DATE NOT NULL,
        horario_embarque TIMESTAMP NOT NULL,
        duracao_voo TEXT NOT NULL
    )
''')

conn.commit()

conn.close()