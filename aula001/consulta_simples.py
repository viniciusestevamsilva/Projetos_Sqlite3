import os
import sqlite3

conn = sqlite3.connect("C:/vinicius/sqlite/aula001/arquivo.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM clientes")
resultados = cursor.fetchall()

os.system('cls')
for row in resultados:
    print(row)
conn.close()