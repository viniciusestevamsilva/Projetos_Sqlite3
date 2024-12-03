import sqlite3
from prettytable import PrettyTable


# ========================== COMANDO EXIBIR =============
class Exibir:
    def exibir(self, tabela):
        conn = sqlite3.connect("C:/vinicius/sqlite/projeto_sqlite/aeroporto.db")
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

# ========================== COMANDO ADICIONAR =============
class Adicionar:
    def adicionar(self, tabela):
        conn = sqlite3.connect("C:/vinicius/sqlite/projeto_sqlite/aeroporto.db")
        cursor = conn.cursor()

        print()
        colunas = input('Digite as colunas (separados por vírgula): ').split(',')
        dados = input('Digite os dados (separados por vírgula): ').split(',')

       # o 1° join cria uma lista com as colunas 2°join fazuma lista com os placeholders '?', que os valores que vao ser inseridos
        cursor.execute(f"INSERT INTO {tabela} ({', '.join(colunas)}) VALUES ({', '.join(['?'] * len(colunas))})", dados)
        
        conn.commit()
        conn.close()

# ========================== COMANDO ATUALIZAR =============
class Atualizar:
    def atualizar(self, tabela, identificador, valor):
        conn = sqlite3.connect("C:/vinicius/sqlite/projeto_sqlite/aeroporto.db")
        cursor = conn.cursor()

        print()
        colunas = input('Digite as colunas que seram atualizadas (separados por vírgula): ').split(',')
        dados = input('Digite os novos dados (separados por vírgula): ').split(',')

        
        if len(colunas) != len(dados):
            print('+----------------------------------------+')
            print("+   O número de colunas não corresponde  +")
            print("+      ao número de dados fornecidos.    +")
            return

        # Atualiza os registros
        for i in range(len(colunas)):
            coluna = colunas[i].strip()
            dado = dados[i].strip()  
            cursor.execute(f"UPDATE {tabela} SET {coluna} = ? WHERE {identificador} = ?", (dado, valor))

        
        conn.commit()
        conn.close()


# ========================== COMANDO APAGAR =============
class Apagar:
    def apagar(self, tabela, identificador, valor):
        conn = sqlite3.connect("C:/vinicius/sqlite/projeto_sqlite/aeroporto.db")
        cursor = conn.cursor()

       
        cursor.execute(f"DELETE FROM {tabela} WHERE {identificador} = ?", (valor,))
        
        conn.commit()
        conn.close()