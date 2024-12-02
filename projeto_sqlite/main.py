import os
import math
import sqlite3
from comandos import Exibir
from comandos import Adicionar
from comandos import Atualizar
from comandos import Apagar




while True:
    os.system('cls')
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
    # elif opcao == 2:
    # elif opcao == 3:
    # elif opcao == 4:

