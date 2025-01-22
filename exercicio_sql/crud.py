import os
import sqlite3
from prettytable import PrettyTable


conn = sqlite3.connect("C:/vinicius/sqlite/exercicio_sql/viagens.db")
conn.execute("PRAGMA foreign_keys = ON;")
cursor = conn.cursor()


class exibir:
    def SELECT(self, tabela):
            
        conn = sqlite3.connect("C:/vinicius/sqlite/exercicio_sql/viagens.db")
        cursor = conn.cursor()
        
        cursor.execute(f'SELECT * FROM {tabela}')
        resultado = cursor.fetchall()

        tabela_formatada = PrettyTable()

        colunas = [descricao[0] for descricao in cursor.description]
        tabela_formatada.field_names = colunas
            
        for row in resultado:
            tabela_formatada.add_row(row)

        print(tabela_formatada) 
        conn.close()