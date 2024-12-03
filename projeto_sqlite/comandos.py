import sqlite3
from prettytable import PrettyTable


class Exibir:
    def __init__(self, tabela):
        self.tabela = tabela
        
    def exibir(self, tabela):
        self.tabela = tabela
        
        conn = sqlite3.connect("C:/vinicius/sqlite/projeto_sqlite/aeroporto.db")
        cursor = conn.cursor()

        cursor.execute(f'SELECT * FROM {tabela}')
        resultado = cursor.fetchall()
        
        tabela = PrettyTable()
        
        colunas = [descricao[0] for descricao in cursor.description]

        tabela.field_names = colunas

        for row in resultado:
            tabela.add_row(row)

            print(tabela)
            conn.close()
        return resultado
    


class Adicionar:
    def __init__(self, nome, cpf, data_de_nascimento, classe, assento):
        self.nome = nome
        self.cpf = cpf(int)
        self.data_de_nascimento = data_de_nascimento
        self.classe = classe
        self.assento = assento(int)
        
    def adcionar(self):
        conn = sqlite3.connect("C:/vinicius/sqlite/projeto_sqlite/aeroporto.db");
        cursor = conn.cursor()
        
        nome = input('Insira o nome: ')
        cpf = input('Insira o CPF: ')
        data_de_nascimento = input('Insira a data de nascimento: ')
        classe = input('Digite sua classe: ')
        assento = input('Digite seu assento: ')
        dados_inseridos = (self.nome,self.cpf,self.data_de_nascimento,self.classe,self.assento)
        
        cursor.executemany(
            "INSERT INTO clientes (nome, cpf, data_de_nascimento, classe, assento) VALUES (?,?,?,?,?)", dados_inseridos)
        conn.commit()
        conn.close()


class Atualizar:
    def __init__(self):
        
    def atualizar(self):
        conn = sqlite3.connect("C:/vinicius/sqlite/projeto_sqlite/aeroporto.db")
        cursor = conn.cursor()
        
        cursor.execute("UPDATE ? SET ? = ? WHERE ? = ?",
            ())
        conn.commit()
        conn.close()

class Apagar:
    def __init__(self):
        
    def apagar(self):
        conn = sqlite3.connect("C:/vinicius/sqlite/projeto_sqlite/aeroporto.db")
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM ? WHERE  ?", {})
        conn.commit()
        conn.close()
