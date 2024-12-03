import sqlite3
from prettytable import PrettyTable


class Exibir:
    def exibir(self, tabela):
        conn = sqlite3.connect("C:/vinicius/sqlite/projeto_sqlite/bd_aeroporto.db")
        cursor = conn.cursor()

        # Exibe todos os registros de qualquer tabela
        cursor.execute(f'SELECT * FROM {tabela}')
        resultado = cursor.fetchall()

        # Cria a tabela formatada com PrettyTable
        tabela_formatada = PrettyTable()

        # Obtém os nomes das colunas
        colunas = [descricao[0] for descricao in cursor.description]
        tabela_formatada.field_names = colunas

        # Adiciona as linhas à tabela
        for row in resultado:
            tabela_formatada.add_row(row)

        print(tabela_formatada)  # Imprime a tabela
        conn.close()


class Adicionar:
    def adicionar(self, tabela):
        conn = sqlite3.connect("C:/vinicius/sqlite/projeto_sqlite/bd_aeroporto.db")
        cursor = conn.cursor()

        # Solicita ao usuário os dados para inserir
        campos = input('Digite os campos (separados por vírgula): ').split(',')
        dados = input('Digite os dados (separados por vírgula): ').split(',')

        # Usa a função executemany para inserir dados na tabela
        cursor.execute(f"INSERT INTO {tabela} ({', '.join(campos)}) VALUES ({', '.join(['?'] * len(campos))})", dados)
        
        conn.commit()
        conn.close()


class Atualizar:
    def atualizar(self, tabela, identificador, valor):
        conn = sqlite3.connect("C:/vinicius/sqlite/projeto_sqlite/bd_aeroporto.db")
        cursor = conn.cursor()

        # Solicita ao usuário os dados a serem atualizados
        campos = input('Digite os campos a serem atualizados (separados por vírgula): ').split(',')
        dados = input('Digite os novos dados (separados por vírgula): ').split(',')

        # Cria um dicionário com os campos e dados
        campos_e_dados = dict(zip(campos, dados))

        # Atualiza o registro usando o identificador
        for campo, dado in campos_e_dados.items():
            cursor.execute(f"UPDATE {tabela} SET {campo} = ? WHERE {identificador} = ?", (dado, valor))
        
        conn.commit()
        conn.close()


class Apagar:
    def apagar(self, tabela, identificador, valor):
        conn = sqlite3.connect("C:/vinicius/sqlite/projeto_sqlite/bd_aeroporto.db")
        cursor = conn.cursor()

        # Apaga o registro baseado no identificador
        cursor.execute(f"DELETE FROM {tabela} WHERE {identificador} = ?", (valor,))
        
        conn.commit()
        conn.close()

