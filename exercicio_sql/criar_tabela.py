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
    CREATE TABLE IF NOT EXISTS voos(
        
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS (
        
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS (

        )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS (
        
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS (
        
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS (
        
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS (
        
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS (
        
    )
''')