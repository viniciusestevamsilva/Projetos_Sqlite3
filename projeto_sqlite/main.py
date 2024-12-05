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
        
        if tabela == '' and tabela == int: # Ve se a tabela não esta vazia 
            os.system('cls') 
            print('+------------------------------+')
            print('Opção inválida. Tente novamente.')
            print('+------------------------------+') 
            input('Pressione ENTER para voltar')
            
        else:
            exibir = Exibir()
            exibir.SELECT(tabela)
            input('Pressione ENTER para voltar')

# ========================== ADICIONAR =============
    elif opcao == '2':
            os.system('cls') 
            print('+-------------------+')
            print('+    Adicionando    +')
            print('+-------------------+')
            tabela = input('Digite o nome da tabela para adicionar: ')
            
            # Verificação se são válidos e se não estao vazios
            if not tabela or not isinstance(tabela, str):
                os.system('cls') 
                print('+------------------------------+')
                print('Opção inválida. Tente novamente.')
                print('+------------------------------+') 
                input('Pressione ENTER para voltar')
                
            else:
            
                adicionar = Adicionar()
                adicionar.INSERT(tabela)
                os.system('cls')
                print('+--------------------------------------+')
                print('+    Registro Adicionado com sucesso!  +')
                print('+--------------------------------------+')
                input('Pressione ENTER para voltar')
                
                
# ========================== ATUALIZAR =============
    elif opcao == '3': 
        os.system('cls') 
        print('+-------------------+')
        print('+    Atualizando    +')
        print('+-------------------+')
        tabela = input('Digite o nome da tabela para atualizar: ')
        
        # Verificação se são válidos e se não estao vazios
        if not tabela or not isinstance(tabela, str):
            os.system('cls') 
            print('+------------------------------+')
            print('Opção inválida. Tente novamente.')
            print('+------------------------------+') 
            input('Pressione ENTER para voltar')
            continue

        identificador = input('Digite o identificador (ex: cpf ou id): ')
        
        if not identificador or not isinstance(identificador, str):
            os.system('cls') 
            print('+------------------------------+')
            print('Opção inválida. Tente novamente.')
            print('+------------------------------+') 
            input('Pressione ENTER para voltar')
            continue


        valor = input(f'Digite o valor do {identificador} para atualizar: ')
        
        if not valor or not isinstance(valor, str):
            os.system('cls') 
            print('+------------------------------+')
            print('Opção inválida. Tente novamente.')
            print('+------------------------------+') 
            input('Pressione ENTER para voltar')
            continue

        
        atualizar = Atualizar()
        atualizar.UPDATE(tabela, identificador, valor)
        os.system('cls')
        print('+---------------------------------------+')
        print('+    Registro Atualizado com sucesso !  +')
        print('+---------------------------------------+')
        input('+      Pressione ENTER para voltar      +')
    
    
# ==========================  APAGAR =============
    elif opcao == '4':
        os.system('cls') 
        print('+----------------+')
        print('+    Apagando    +')
        print('+----------------+')
        tabela = input('Digite o nome da tabela para apagar: ')

        # Verificação se são válidos e se não estao vazios
        if not tabela or not isinstance(tabela, str):
            os.system('cls') 
            print('+------------------------------+')
            print('Opção inválida. Tente novamente.')
            print('+------------------------------+') 
            input('Pressione ENTER para voltar')
            continue

        identificador = input('Digite o identificador (ex: cpf ou id): ')
        
        if not identificador or not isinstance(identificador, str):
            os.system('cls') 
            print('+------------------------------+')
            print('Opção inválida. Tente novamente.')
            print('+------------------------------+') 
            input('Pressione ENTER para voltar')
            continue

        valor = input(f'Digite o valor do {identificador} para apagar: ')
        
        if not valor or not isinstance(valor, str):
            os.system('cls') 
            print('+------------------------------+')
            print('Opção inválida. Tente novamente.')
            print('+------------------------------+') 
            input('Pressione ENTER para voltar')
            continue
        
        apagar = Apagar()
        apagar.DELETE(tabela, identificador, valor)
        os.system('cls')
        print('+------------------------------------+')
        print('+    Registro apagado com sucesso !  +')
        print('+------------------------------------+')
        input('+    Pressione ENTER para voltar     +')
    
    
# ========================== OPÇÃO INVALIDA =============
    else:
        os.system('cls') 
        print('+------------------------------+')
        print('Opção inválida. Tente novamente.')
        print('+------------------------------+')
        input('Pressione ENTER para voltar')