import os
import sqlite3
import time
from crud import Exibir
from crud import Adicionar
from crud import Atualizar
from crud import Apagar

# Conectando com banco de dados
conn = sqlite3.connect("C:/vinicius/sqlite/exercicio_sql/viagens.db")
conn.execute("PRAGMA foreign_keys = ON;")

while True:
    os.system('cls')
    print('+---------------------------+')
    print('|  Passagens Trivago |')
    print('+---------------------------+')
    print('| 1 - Verificar Disponibilidade de Voos |')
    print('| 2 - Comprar Passagem                 |')
    print('| 3 - Alterar Dados de Passagem        |')
    print('| 4 - Cancelar Passagem               |')
    print('| 5 - Finalizar Compra                |')
    print('+---------------------------+')

    opcao = input('Escolha uma opção: ')
    os.system('cls')

# ========================== FINALIZAÇÃO ============= 
    if opcao == '5':
        os.system('cls') 
        print('+---------------------------+')
        print('|    Compra finalizada!      |')
        print('+---------------------------+')
        print('|   Obrigado por utilizar   |')
        print('|       nosso serviço!      |')
        print('+---------------------------+')
        
        time.sleep(3)
        os.system('cls')
        break

# ========================== VERIFICAR VOOS DISPONÍVEIS ============= 
    elif opcao == '1':
        os.system('cls')
        print('+------------------------+')
        print('|  Verificando Disponibilidade de Voos |')
        print('+------------------------+')
        tabela = 'voos'  # Aqui o código mostra a tabela de voos disponíveis
        
        exibir = Exibir()
        exibir.SELECT(tabela)
        
        print('| Escolha um voo e continue para comprar |')
        print('+---------------------------------------+')
        input('|  Pressione ENTER para voltar          |')

# ========================== COMPRAR PASSAGEM ============= 
    elif opcao == '2':
        while True:
            os.system('cls')
            print('+-----------------------+')
            print('| Comprar Passagem      |')
            print('+-----------------------+')
            print('Disponibilidade de Voos: ')
            tabela = 'voos'  # Mostra a tabela de voos disponíveis
            exibir = Exibir()
            exibir.SELECT(tabela)
            
            voo_id = input('Digite o ID do voo para comprar: ')
            
            if voo_id:
                # O código aqui pode adicionar um registro na tabela de passagens
                adicionar = Adicionar()
                adicionar.INSERT('minha_passagens')  # Adiciona a passagem comprada na tabela de passagens
                print('| Passagem comprada com sucesso! |')
                exibir = Exibir()
                exibir.SELECT(tabela)
                
                print('| Deseja comprar outra passagem? |')
                print('| Sim(s) ou Não(n) |')
                opcao = input('- :')
                if opcao == 'n':
                    break

# ========================== ALTERAR DADOS DE PASSAGEM ============= 
    elif opcao == '3':
        while True:
            os.system('cls')
            print('+------------------------+')
            print('| Alterar Dados de Passagem |')
            print('+------------------------+')
            tabela = 'minha_passagens'  # Mostra a tabela de passagens compradas
            exibir = Exibir()
            exibir.SELECT(tabela)
            
            # O código permite que o cliente altere dados da passagem comprada
            identificador = input('Digite o identificador (ID) da passagem para alterar: ')
            valor = input(f'Digite o novo valor para o identificador {identificador}: ')
            
            if identificador and valor:
                atualizar = Atualizar()
                atualizar.UPDATE('minha_passagens', 'id_passagem', identificador)
                print('| Dados da passagem atualizados com sucesso! |')
                exibir = Exibir()
                exibir.SELECT(tabela)
                
                print('| Deseja alterar outra passagem? |')
                print('| Sim(s) ou Não(n) |')
                opcao = input('- :')
                if opcao == 'n':
                    break

# ========================== CANCELAR PASSAGEM ============= 
    elif opcao == '4':
        while True:
            os.system('cls')
            print('+-----------------------+')
            print('| Cancelar Passagem     |')
            print('+-----------------------+')
            tabela = 'minha_passagens'  # Mostra a tabela de passagens compradas
            exibir = Exibir()
            exibir.SELECT(tabela)
            
            identificador = input('Digite o identificador (ID) da passagem para cancelar: ')
            if identificador:
                apagar = Apagar()
                apagar.DELETE('minha_passagens', 'id_passagem', identificador)  # Apaga a passagem
                print('| Passagem cancelada com sucesso! |')
                exibir = Exibir()
                exibir.SELECT(tabela)
                
                print('| Deseja cancelar outra passagem? |')
                print('| Sim(s) ou Não(n) |')
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