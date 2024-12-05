import sqlite3
from prettytable import PrettyTable
import os

# ========================== COMANDO EXIBIR =============
class Exibir:
    def SELECT(self, tabela):
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
    def INSERT(self, tabela):
        conn = sqlite3.connect("C:/vinicius/sqlite/projeto_sqlite/aeroporto.db")
        cursor = conn.cursor()
        
        # verifica se a tabela não esta vazia ou se é uma instancia invalida
        if not tabela or not isinstance(tabela, str):
            os.system('cls') 
            print('+------------------------------+')
            print('Opção inválida. Tente novamente.')
            print('+------------------------------+') 
            input('Pressione ENTER para voltar')
            return

        conn = sqlite3.connect("C:/vinicius/sqlite/projeto_sqlite/aeroporto.db")
        cursor = conn.cursor()


        colunas = input('Digite as colunas (separados por vírgula): ').split(',')
        dados = input('Digite os dados (separados por vírgula): ').split(',')
        
        # Verifica se as colunas ou dados estão vazios
        if not colunas or not dados or len(colunas) != len(dados):
            os.system('cls') 
            print('+------------------------------+')
            print('Opção inválida. Tente novamente.')
            print('+------------------------------+') 
            input('Pressione ENTER para voltar')
            return

        cursor.execute(f"INSERT INTO {tabela} ({', '.join(colunas)}) VALUES ({', '.join(['?'] * len(colunas))})", dados)
        
        conn.commit()
        conn.close()

# ========================== COMANDO ATUALIZAR =============
class Atualizar:
    def UPDATE(self, tabela, identificador, valor):
        conn = sqlite3.connect("C:/vinicius/sqlite/projeto_sqlite/aeroporto.db")
        cursor = conn.cursor()
        
        # Verificação se são válidos e se não estao vazios
        if not tabela or not isinstance(tabela, str):
            os.system('cls') 
            print('+------------------------------+')
            print('Opção inválida. Tente novamente.')
            print('+------------------------------+') 
            input('Pressione ENTER para voltar')
            return

        if not identificador or not isinstance(identificador, str):
            os.system('cls') 
            print('+------------------------------+')
            print('Opção inválida. Tente novamente.')
            print('+------------------------------+') 
            input('Pressione ENTER para voltar')
            return

        if not valor or not isinstance(valor, str):
            os.system('cls') 
            print('+------------------------------+')
            print('Opção inválida. Tente novamente.')
            print('+------------------------------+') 
            input('Pressione ENTER para voltar')
            return

        colunas = input('Digite as colunas que serão atualizadas (separadas por vírgulas): ').split(',')
        dados = input('Digite os novos dados (separadas por vírgulas): ').split(',')

        if len(colunas) != len(dados):
            print('+----------------------------------------+')
            print("+   O número de colunas não corresponde  +")
            print("+      ao número de dados fornecidos.    +")
            print('+----------------------------------------+')
            input('Pressione ENTER para voltar')
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
    def DELETE(self, tabela, identificador, valor):
        conn = sqlite3.connect("C:/vinicius/sqlite/projeto_sqlite/aeroporto.db")
        cursor = conn.cursor()
        
        # Verificação se são válidos e se não estao vazios
        if not tabela or not isinstance(tabela, str):
            os.system('cls') 
            print('+------------------------------+')
            print('Opção inválida. Tente novamente.')
            print('+------------------------------+') 
            input('Pressione ENTER para voltar')
            return

        if not identificador or not isinstance(identificador, str):
            os.system('cls') 
            print('+------------------------------+')
            print('Opção inválida. Tente novamente.')
            print('+------------------------------+') 
            input('Pressione ENTER para voltar')
            return

        if not valor or not isinstance(valor, str):
            os.system('cls') 
            print('+------------------------------+')
            print('Opção inválida. Tente novamente.')
            print('+------------------------------+') 
            input('Pressione ENTER para voltar')
            return

        cursor.execute(f"DELETE FROM {tabela} WHERE {identificador} = ?", (valor,))

        conn.commit()
        conn.close()