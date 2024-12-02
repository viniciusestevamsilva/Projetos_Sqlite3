import sqlite3


class Exibir:
    def exibir(self):
        conn = sqlite3.connect("C:/vinicius/sqlite/projeto_sqlite/bd_viagens.py")
        cursor = conn.cursor()

        cursor.execute(f'SELECT * FROM {self.tabela}')
        resultado = cursor.fetchall()

        return resultado


class Adicionar:
    conn = sqlite3.connect("C:/vinicius/sqlite/projeto_sqlite/bd_viagens.py")
    cursor = conn.cursor()


class Atualizar:
    conn = sqlite3.connect("C:/vinicius/sqlite/projeto_sqlite/bd_viagens.py")
    cursor = conn.cursor()


class Apagar:
    conn = sqlite3.connect("C:/vinicius/sqlite/projeto_sqlite/bd_viagens.py")
    cursor = conn.cursor()
