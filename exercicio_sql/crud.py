import os
import sqlite3
from prettytable import PrettyTable


conn = sqlite3.connect("C:/vinicius/sqlite/exercicio_sql/viagens.db")
conn.execute("PRAGMA foreign_keys = ON;")
cursor = conn.cursor()

class Exibir:
     def SELECT(self, tabela):
        
        conn = sqlite3.connect("C:/vinicius/sqlite/exercicio_sql/viagens.db")
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
    
    def INSERT(self, tabela):
        conn = sqlite3.connect("C:/vinicius/sqlite/exercicio_sql/viagens.db")
        conn.execute("PRAGMA foreign_keys = ON;")
        cursor = conn.cursor()

        # Verifica se a tabela foi fornecida corretamente
        if not tabela or not isinstance(tabela, str):
            os.system('cls') 
            print('+---------------------------------+')
            print('| Opção inválida. Tente novamente.|')
            print('+---------------------------------+')
            input('|   Pressione ENTER para voltar   |')
            return

        print('+---------------------------+')
        print('|    Deseja adicionar um    |')
        print('|         ou varios?        |')
        print('| 1 - para um               |')
        print('| 2 - para varios           |')
        print('+---------------------------+')
        
        escolha = input('Deseja adicionar um ou vários registros? (1 para um, 2 para vários): ')
        
        if escolha == '1':
            # Obter os dados com base na estrutura esperada para a tabela
            if tabela == 'passageiro':
                colunas = ['nome', 'CPf', 'data_de_nascimento', 'classe', 'assento']
            elif tabela == 'minha_passagens':
                colunas = ['id_passageiro', 'preco', 'duracao_viagem', 'data_viagem', 'origem_destino']
            elif tabela == 'voos':
                colunas = ['origem_destino', 'status_voo', 'passagens_disponiveis', 'preco_passagem', 'companhia_responsavel']
            elif tabela == 'companhias':
                colunas = ['nome_companhia', 'numero_voo', 'avaliacao', 'aviao', 'capacidade']
            else:
                print('Tabela desconhecida')
                return

            dados = input(f'Digite os dados para {", ".join(colunas)} (separados por vírgula): ').split(',')
            
            # Verifica se a quantidade de dados bate com a quantidade de colunas
            if len(dados) != len(colunas):
                os.system('cls') 
                print('+---------------------------------+')
                print('| A quantidade de dados não corresponde à quantidade de colunas.')
                print('+---------------------------------+')
                input('|   Pressione ENTER para voltar   |')
                return

            cursor.execute(f"INSERT INTO {tabela} ({', '.join(colunas)}) VALUES ({', '.join(['?'] * len(colunas))})", dados)
            conn.commit()

        elif escolha == '2':
            dados_lista = []
            while True:
                if tabela == 'passageiro':
                    colunas = ['nome', 'CPf', 'data_de_nascimento', 'classe', 'assento']
                elif tabela == 'minha_passagens':
                    colunas = ['id_passageiro', 'preco', 'duracao_viagem', 'data_viagem', 'origem_destino']
                elif tabela == 'voos':
                    colunas = ['origem_destino', 'status_voo', 'passagens_disponiveis', 'preco_passagem', 'companhia_responsavel']
                elif tabela == 'companhias':
                    colunas = ['nome_companhia', 'numero_voo', 'avaliacao', 'aviao', 'capacidade']
                else:
                    print('Tabela desconhecida')
                    return

                dados = input(f'Digite os dados do próximo registro para {", ".join(colunas)} (separados por vírgula): ')
                print('Digite "parar" para finalizar')
                
                if dados.lower() == 'parar':
                    break
                
                dados_lista.append(dados.split(','))

            if not dados_lista:
                os.system('cls') 
                print('+---------------------------------+')
                print('| Não há registros para adicionar.|')
                print('+---------------------------------+')
                input('|   Pressione ENTER para voltar   |')
                return

            cursor.executemany(f"INSERT INTO {tabela} ({', '.join(colunas)}) VALUES ({', '.join(['?'] * len(colunas))})", dados_lista)
            conn.commit()

        conn.close()

class Atualizar:
    
    def UPDATE(self, tabela, identificador, valor):
        
        conn = sqlite3.connect("C:/vinicius/sqlite/exercicio_sql/viagens.db")
        conn.execute("PRAGMA foreign_keys = ON;")
        cursor = conn.cursor()
        
        # Verifica se a tabela é válida
        if not tabela or not isinstance(tabela, str):
            os.system('cls') 
            print('+---------------------------------+')
            print('| Opção inválida. Tente novamente.|')
            print('+---------------------------------+')
            input('|   Pressione ENTER para voltar   |')
            return
        
        # Verifica se o identificador e valor são válidos
        if not identificador or not isinstance(identificador, str):
            os.system('cls') 
            print('+---------------------------------+')
            print('| Identificador inválido. Tente novamente.|')
            print('+---------------------------------+')
            input('|   Pressione ENTER para voltar   |')
            return

        if not valor or not isinstance(valor, str):
            os.system('cls') 
            print('+---------------------------------+')
            print('| Valor inválido. Tente novamente.|')
            print('+---------------------------------+')
            input('|   Pressione ENTER para voltar   |')
            return
        
        # Determina as colunas com base na tabela
        if tabela == 'passageiro':
            colunas = ['nome', 'CPf', 'data_de_nascimento', 'classe', 'assento']
        elif tabela == 'minha_passagens':
            colunas = ['id_passageiro', 'preco', 'duracao_viagem', 'data_viagem', 'origem_destino']
        elif tabela == 'voos':
            colunas = ['origem_destino', 'status_voo', 'passagens_disponiveis', 'preco_passagem', 'companhia_responsavel']
        elif tabela == 'companhias':
            colunas = ['nome_companhia', 'numero_voo', 'avaliacao', 'aviao', 'capacidade']
        else:
            print('Tabela desconhecida.')
            return

        # Solicita os dados para atualização
        colunas_atualizar = input(f'Digite as colunas que deseja atualizar para {", ".join(colunas)} (separadas por vírgula): ').split(',')
        dados = input(f'Digite os novos dados para {", ".join(colunas_atualizar)} (separados por vírgula): ').split(',')

        # Verifica se o número de colunas e dados corresponde
        if len(colunas_atualizar) != len(dados):
            print('+----------------------------------------+')
            print("| O número de colunas não corresponde ao número de dados fornecidos. |")
            print('+----------------------------------------+')
            input('Pressione ENTER para voltar.')
            return
        
        # Atualiza os dados
        for i in range(len(colunas_atualizar)):
            coluna = colunas_atualizar[i].strip()
            dado = dados[i].strip()  
            cursor.execute(f"UPDATE {tabela} SET {coluna} = ? WHERE {identificador} = ?", (dado, valor))

        conn.commit()
        conn.close()

class Apagar:
    
    def DELETE(self, tabela, identificador, valor):
        conn = sqlite3.connect("C:/vinicius/sqlite/exercicio_sql/viagens.db")
        conn.execute("PRAGMA foreign_keys = ON;")
        cursor = conn.cursor()
        
        # Verifica se a tabela e os parâmetros são válidos
        if not tabela or not isinstance(tabela, str):
            os.system('cls') 
            print('+---------------------------------+')
            print('| Opção inválida. Tente novamente.|')
            print('+---------------------------------+')
            input('|   Pressione ENTER para voltar   |')
            return

        if not identificador or not isinstance(identificador, str):
            os.system('cls') 
            print('+---------------------------------+')
            print('| Identificador inválido. Tente novamente.|')
            print('+---------------------------------+')
            input('|   Pressione ENTER para voltar   |')
            return

        if not valor or not isinstance(valor, str):
            os.system('cls') 
            print('+---------------------------------+')
            print('| Valor inválido. Tente novamente.|')
            print('+---------------------------------+')
            input('|   Pressione ENTER para voltar   |')
            return
        
        # Deleta o registro
        cursor.execute(f"DELETE FROM {tabela} WHERE {identificador} = ?", (valor,))
        conn.commit()
        conn.close()