import os
import sqlite3
from crud import Exibir
from crud import Adicionar
from crud import Atualizar
from crud import Apagar

# Conectar ao banco de dado
conn = sqlite3.connect("C:/vinicius/sqlite/projeto_sqlite/aeroporto.db")
   
while True:
    os.system('cls') 
    print('+-----------------+          +-------------------+')
    print('+ MENU COMANDOS   +          +      TABELAS      +')
    print('+-----------------+          +-------------------+')
    print('+ 1 - Exibir      +          +   companhia_aerea +')
    print('+ 2 - Adicionar   +          +      passageiro   +')
    print('+ 3 - Atualizar   +          +  terminal_viagens +')
    print('+ 4 - Apagar      +          +       ticket      +')
    print('+ 5 - Finalizar   +          +                   +')
    print('+-----------------+          +-------------------+')

    opcao = input('Opção escolhida: ')

# ========================== FINALIZAÇÃO =============
    if opcao == '5':
        os.system('cls') 
        print('+--------------------------+')
        print('+    Programa finalizado   +')
        print('+--------------------------+')
        break

# ========================== EXIBIR =============
    elif opcao == '1':
        os.system('cls') 
        print('+---------------+')
        print('+    Exibindo   +')
        print('+---------------+')
        tabela = input('Digite o nome da tabela para exibir: ')
        
        if tabela == '' and tabela == int:
            os.system('cls') 
            print('+------------------------------+')
            print('Opção inválida. Tente novamente.')
            print('+------------------------------+') 
            input('Pressione ENTER para voltar')
            
        else:
            exibir = Exibir()
            exibir.exibir(tabela)
            input('Pressione ENTER para voltar')

# ========================== ADICIONAR =============
    elif opcao == '2':
        os.system('cls') 
        print('+-------------------+')
        print('+    Adicionando    +')
        print('+-------------------+')
        tabela = input('Digite o nome da tabela para adicionar: ')
        adicionar = Adicionar()
        adicionar.adicionar(tabela)
        print('+--------------------------------------+')
        print('+    Registro Adcionado com sucesso !  +')
        input('+    Pressione ENTER para voltar       +')
        
# ========================== ATUALIZAR =============
    elif opcao == '3':
        os.system('cls') 
        print('+-------------------+')
        print('+    Atualizando    +')
        print('+-------------------+')
        tabela = input('Digite o nome da tabela para atualizar: ')
        identificador = input('Digite o identificador (ex: cpf ou id): ')
        valor = input(f'Digite o valor do {identificador} para atualizar: ')
        atualizar = Atualizar()
        atualizar.atualizar(tabela, identificador, valor)
        print('+---------------------------------------+')
        print('+    Registro Atualizado com sucesso !  +')
        input('+      Pressione ENTER para voltar      +')

# ==========================  APAGAR =============
    elif opcao == '4':
        os.system('cls') 
        print('+----------------+')
        print('+    Apagando    +')
        print('+----------------+')
        tabela = input('Digite o nome da tabela para apagar: ')
        identificador = input('Digite o identificador (ex: cpf ou id): ')
        valor = input(f'Digite o valor do {identificador} para apagar: ')
        apagar = Apagar()
        apagar.apagar(tabela, identificador, valor)
        print('+------------------------------------+')
        print('+    Registro apagado com sucesso !  +')
        input('+    Pressione ENTER para voltar     +')

# ========================== OPÇÃO INVALIDA =============
    else:
        os.system('cls') 
        print('+------------------------------+')
        print('Opção inválida. Tente novamente.')
        print('+------------------------------+')
        input('Pressione ENTER para voltar')
