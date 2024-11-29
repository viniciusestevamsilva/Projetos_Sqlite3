import os
import sqlite3
from prettytable import PrettyTable

conn = sqlite3.connect("C:/vinicius/sqlite/aula001/arquivo.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM clientes")
resultados = cursor.fetchall()

os.system('cls')

# Cria a tabela Prettytable e define os nomes das colunas
tabela = PrettyTable()
# Obtém os nomes das colunas a partit de cursor.description
colunas = [descricao[0] for descricao in cursor.description]
# Define os nomes das colunas na tabela Prettytable
tabela.field_names = colunas

# Adiciona as linhas á tabela
for row in resultados:
    tabela.add_row(row)

print(tabela)
conn.close()