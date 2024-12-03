# Curso de Desenvolvimentos de Sistemas
# Autor: Vinícius Estevam da Silva
# Data: 29/11/2007

import sqlite3

conn = sqlite3.connect("C:/vinicius/sqlite/projeto_sqlite/aeroporto.db")

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS passageiro (
        id_passageiro PRIMARY KEY INTEGER AUTOINCREMENT,
        nome TEXT NOT NULL,
        CPF INTEGER NOT NULL,
        data_de_nascimento DATA NOT NULL,
        classe TEXT NOT NULL,
        assento TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS terminial_viagens (
        status_voo TEXT NOT NULL,
        horario embarque TIMESTAMP NOT NULL,
        Destino TEXT NOT NULL,
        portao INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS companhia_aerea (
        id_voo INTEGER PRIMARY KEY AUTOINCREMENT,
        id_aviao INTEGER NOT NULL
        numero_voo INTEGER NOT NULL,
        nome_companhia TEXT NOT NULL
        )''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS ticket (
        ticket id INTEGER PRIMARY KEY AUTOINCREMENT,
        preco REAL NOT NULL,
        origem_destino TEXT NOT NULL,
        data_voo DATE NOT NULL,
        horario_embarque TIMESTAMP NOT NULL,
        duracao_voo TEXT NOT NULL
    )
''')

conn.commit()
conn.close()