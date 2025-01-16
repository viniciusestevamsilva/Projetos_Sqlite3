# Curso de Desenvolvimento de sistemas
# Autor: Vinícius Estevam da Silva
# Data: 11/12/2024

import os
import sqlite3
import time
from crud import Exibir
from crud import Adicionar
from crud import Atualizar
from crud import Apagar

# Conectando com banco de dado
conn = sqlite3.connect("C:/vinicius/sqlite/atividade_sqlite/aeroporto.db")
conn.execute("PRAGMA foreign_keys = ON;") # ativar o ON DELETE CASCADE
   
while True:
    
    os.system('cls') 
    print('+-----------------+          +--------------------------------------+')
    print('| MENU COMANDOS   |          |                  TABELAS             |')
    print('+-----------------+          +--------------------------------------+')
    print('| 1 - Exibir      |          |       aviao       | terminal viagens |')
    print('| 2 - Adicionar   |          |  companhia aerea  |       ticket     |')
    print('| 3 - Atualizar   |          |  pagamento ticket |        voo       |')
    print('| 4 - Apagar      |          |     passageiro    |                  |')
    print('| 5 - Finalizar   |          |        rota       |                  |')
    print('+-----------------+          +--------------------------------------+')

    opcao = input('Opção escolhida: ')

# ========================== FINALIZAÇÃO =============
    if opcao == '5':
        
        os.system('cls') 
        print('+--------------------------+         +----------------------------------------+')
        print('|    Programa finalizado   |         |   Este programa foi feito em Python    |')
        print('+--------------------------+         |   com o uso do SQLite3. Por enquanto   |')
        print('|  Obrigado pelo seu tempo |         |   esta sem relacionamento nas tabelas  |')
        print('+--------------------------+         +----------------------------------------+')
        
        time.sleep(3)
        os.system('cls')
        break


# ========================== EXIBIR =============
    elif opcao == '1':
        
        os.system('cls') 
        print('+---------------+')
        print('|    Exibindo   |')
        print('+---------------+')
        tabela = input('Digite o nome da tabela para exibir: ')
        
        if tabela == '' and tabela == int: # Ve se a tabela não esta vazia
            
            os.system('cls') 
            print('+---------------------------------+')
            print('| Opção inválida. Tente novamente.|')
            print('+---------------------------------+')
            input('|   Pressione ENTER para voltar   |')
            
        else:
            
            os.system('cls')
            
            exibir = Exibir() # exibi a tabela escolhida
            exibir.SELECT(tabela)
            
            print(f'| Exibindo a tabela: {tabela}')
            print('+------------------------------------+')
            input('|    Pressione ENTER para voltar     |')


# ========================== ADICIONAR =============
    elif opcao == '2':
        
        while True: 
            
            os.system('cls') 
            print('+---------------------------+')
            print('|         Adicionando       |')
            print('+---------------------------+')
            tabela = input('Digite o nome da tabela para adicionar: ')
            
            os.system('cls')
            exibir = Exibir()
            exibir.SELECT(tabela)
            
            print(f'| Exibindo a tabela: {tabela}')
            
            if not tabela or not isinstance(tabela, str):
                
                os.system('cls') 
                print('+---------------------------------+')
                print('| Opção inválida. Tente novamente.|')
                print('+---------------------------------+')
                input('|   Pressione ENTER para voltar   |')
                continue
            
            else:
                adicionar = Adicionar() # adiciona na tabela escolhida
                adicionar.INSERT(tabela)
                
                os.system('cls')
                exibir = Exibir()
                exibir.SELECT(tabela)
                
                print('|    Registro Adicionado com sucesso!  |')
                print('+--------------------------------------+')
                print('|        Deseja adicionar outro?       |')
                print('|           Sim(s) ou Não(n)           |')
                opcao = input('| - :')
            
                if opcao == 'n':
                    break 
                
                
# ========================== ATUALIZAR =============
    elif opcao == '3':
        
        while True: 
            
            os.system('cls') 
            print('+-------------------+')
            print('|    Atualizando    |')
            print('+-------------------+')
            tabela = input('Digite o nome da tabela para atualizar: ')
            
            os.system('cls')
            exibir = Exibir() # exibi a tabela escolhida
            exibir.SELECT(tabela)
            
            # Verifica se são válidos e se não estão vazios
            if not tabela or not isinstance(tabela, str):
                
                os.system('cls') 
                print('+---------------------------------+')
                print('| Opção inválida. Tente novamente.|')
                print('+---------------------------------+')
                input('|   Pressione ENTER para voltar   |')
                continue

            identificador = input('Digite o identificador (id): ')
            
            if not identificador or not isinstance(identificador, str):
                
                os.system('cls') 
                print('+---------------------------------+')
                print('| Opção inválida. Tente novamente.|')
                print('+---------------------------------+')
                input('|   Pressione ENTER para voltar   |')
                continue

            valor = input(f'Digite o valor do {identificador} para atualizar: ')
            
            if not valor or not isinstance(valor, str):
                
                os.system('cls') 
                print('+---------------------------------+')
                print('| Opção inválida. Tente novamente.|')
                print('+---------------------------------+')
                input('|   Pressione ENTER para voltar   |')
                continue

            atualizar = Atualizar() # atualiza a tabela escolhida
            atualizar.UPDATE(tabela, identificador, valor)
            
            os.system('cls')
            exibir = Exibir() # exibi a tabela escolhida
            exibir.SELECT(tabela)
            
            print('|    Registro Atualizado com sucesso !  |')
            print('+---------------------------------------+')
            print('|        Deseja atualizar outro?        |')
            print('|           Sim(s) ou Não(n)            |')
            opcao = input('- :')
            if opcao == 'n':
                break 

    
# ==========================  APAGAR =============
    elif opcao == '4':
        
        while True:
            
            os.system('cls') 
            print('+----------------+')
            print('|    Apagando    |')
            print('+----------------+')
            tabela = input('Digite o nome da tabela para apagar: ')

            os.system('cls')
            exibir = Exibir() # exibi a tabela escolhida
            exibir.SELECT(tabela)
            
            # Verificação se são válidos e se não estão vazios
            if not tabela or not isinstance(tabela, str):
                
                os.system('cls')
                print('+---------------------------------+')
                print('| Opção inválida. Tente novamente.|')
                print('+---------------------------------+')
                input('|   Pressione ENTER para voltar   |')
                continue
            
            identificador = input('Digite o identificador (id) \nExemplo: id_passageiro: ')
            
            if not identificador or not isinstance(identificador, str):
                
                os.system('cls') 
                print('+---------------------------------+')
                print('| Opção inválida. Tente novamente.|')
                print('+---------------------------------+')
                input('|   Pressione ENTER para voltar   |')
                continue

            valor = input(f'Digite o valor do {identificador} para apagar: ')
            
            if not valor or not isinstance(valor, str):
                
                os.system('cls') 
                print('+---------------------------------+')
                print('| Opção inválida. Tente novamente.|')
                print('+---------------------------------+')
                input('|   Pressione ENTER para voltar   |')
                continue
            
            apagar = Apagar()
            apagar.DELETE(tabela, identificador, valor) # apaga o registro da tabela escolhida
            
            os.system('cls')
            exibir = Exibir() # exibi a tabela escolhida
            exibir.SELECT(tabela)
            
            print('|    Registro apagado com sucesso !  |')
            print('+------------------------------------+')
            print('|        Deseja apagar outro?        |')
            print('|         Sim(s) ou Não(n)           |')
            opcao = input('- :')
            if opcao == 'n':
                break 

    
# ========================== OPÇÃO INVALIDA =============
    else:
        
        os.system('cls') 
        print('+---------------------------------+')
        print('| Opção inválida. Tente novamente.|')
        print('+---------------------------------+')
        input('|   Pressione ENTER para voltar   |')