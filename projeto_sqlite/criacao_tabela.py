# Curso de Desenvolvimentos de Sistemas
# Autor: Vinícius Estevam da Silva
# Data: 29/11/2007

import sqlite3

conn = sqlite3.connect("C:/vinicius/sqlite/projeto_sqlite/bd_viagens.py")

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS passageiro (
        id passageiro PRIMARY KEY INTEGER AUTOINCREMENT,
        nome TEXT NOT NULL,
        CPF TEXT NOT NULL,
        data de nascimento DATA NOT NULL ,
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS terminial_viagens (
        id_voo INTEGER PRIMARY KEY AUTOINCREMENT,
        status voo TEXT,
        companhia aerea TEXT,
        horario embarque TIMESTAMP,
        horario despacho TIMESTAMP,
        Destino TEXT NOT NULL,
        portao INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS ticket (
        ticket id INTEGER PRIMARY KEY AUTOINCREMENT,
        preco REAL,
        companhia aerea TEXT,
        plano escolhido TEXT,
        classe TEXT,
        assento TEXT,
        Origem / Destino TEXT NOT NULL,
        data voo DATE NOT NULL,
        horario chegada TIMESTAMP,
        horario embarque TIMESTAMP,
        horario despacho TIMESTAMP,
        duracao do voo TEXT NOT NULL,
        numero voo INTEGER NOT NULL
    )
''')

conn.commit()
conn.close()