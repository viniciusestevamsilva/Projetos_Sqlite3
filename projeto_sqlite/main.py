import os
import sqlite3
from comandos import Exibir
from comandos import Adicionar
from comandos import Atualizar
from comandos import Apagar
conn = sqlite3.connect("C:/vinicius/sqlite/projeto_sqlite/aeroporto.db")



os.system('cls')
while True:

    print('+----------------+')
    print('+    BEM-VINDO   +')
    print('+----------------+')
    print(' 1 - Exibir')
    print(' 2 - Adicionar')
    print(' 3 - Atualizar')
    print(' 4 - Apagar')
    print(' 5 - Finalizar')
    print('+----------------+')
    opcao = ('Opção escolhida: ')

    if opcao == 5:
        print('+----------------+')
        print('Programa finalizado')
        print('+----------------+')
        break

    elif opcao == 1:
        busca = Exibir()
        
    elif opcao == 2:
        nome = input('Insira o nome: ')
        cpf = input('Insira o CPF: ')
        data_de_nascimento = input('Insira a data de nascimento: ')
        classe = input('Digite sua classe: ')
        assento = input('Digite seu assento: ')
        adicionar = Adicionar()
        
    elif opcao == 3:
        atualizar = Atualizar()
        
    elif opcao == 4:
        apagar = Apagar()