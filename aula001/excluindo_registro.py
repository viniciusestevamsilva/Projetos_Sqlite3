import os
import sqlite3

conn = sqlite3.connect("C:/vinicius/sqlite/aula001/arquivo.db")

cursor = conn.cursor()

os.system('cls')

nome_cliente = input('Digite o nome do cliente para excluir: ')

# Executa a exclusão com base no nome fornecido peloi usuário
cursor.execute('DELETE FROM clientes WHERE nome = ?', (nome_cliente,))
conn.commit()

print('Cliente deletado com sucesso!')

# Fecha a conexão
conn.close()