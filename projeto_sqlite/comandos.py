import sqlite3
from prettytable import PrettyTable


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


class Adicionar:
    def adicionar(self, tabela):
        conn = sqlite3.connect("C:/vinicius/sqlite/projeto_sqlite/aeroporto.db")
        cursor = conn.cursor()

       
        campos = input('Digite os campos (separados por vírgula): ').split(',')
        dados = input('Digite os dados (separados por vírgula): ').split(',')

       
        cursor.execute(f"INSERT INTO {tabela} ({', '.join(campos)}) VALUES ({', '.join(['?'] * len(campos))})", dados)
        
        conn.commit()
        conn.close()


class Atualizar:
    def atualizar(self, tabela, identificador, valor):
        # Conexão com o banco de dados
        conn = sqlite3.connect("C:/vinicius/sqlite/projeto_sqlite/aeroporto.db")
        cursor = conn.cursor()

        # Solicita campos e dados
        campos = input('Digite os campos a serem atualizados (separados por vírgula): ').split(',')
        dados = input('Digite os novos dados (separados por vírgula): ').split(',')

        # Verifica se o número de campos e dados é igual
        if len(campos) != len(dados):
            print("O número de campos não corresponde ao número de dados fornecidos.")
            return

        # Atualiza os registros
        for i in range(len(campos)):
            campo = campos[i].strip()  # Remove espaços extras
            dado = dados[i].strip()  # Remove espaços extras
            cursor.execute(f"UPDATE {tabela} SET {campo} = ? WHERE {identificador} = ?", (dado, valor))

        # Confirma a transação e fecha a conexão
        conn.commit()
        conn.close()



class Apagar:
    def apagar(self, tabela, identificador, valor):
        conn = sqlite3.connect("C:/vinicius/sqlite/projeto_sqlite/aeroporto.db")
        cursor = conn.cursor()

       
        cursor.execute(f"DELETE FROM {tabela} WHERE {identificador} = ?", (valor,))
        
        conn.commit()
        conn.close()

