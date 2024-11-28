import sqlite3

conn = sqlite3.connect("C:/vinicius/sqlite/aula001/arquivo.db")


cursor = conn.cursor()

# Definição de uma tupla com os dados
dados_clientes = ("João Silva", 30)

# Place Holders (?, ?): Os pontos de interrogação são usados comoaaaa
# "espaços reservados". Eles  serão substituidos pelos valores da
# tuplas dados_cliente (ou seja, "João Silva" e 30)
# Por quê: usar placeholders é uma pratica recomendada,
# pois previne ataques de injeção SQL.
cursor.execute("INSERT INTO clientes (nome,idade) VALUES (?,?)",dados_clientes)

conn.commit() # Salva a transação no banco de dados
conn.close() # Fecha conexão