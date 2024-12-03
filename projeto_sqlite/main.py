import os
import sqlite3
from comandos import Exibir
from comandos import Adicionar
from comandos import Atualizar
from comandos import Apagar

# Conectar ao banco de dados
conn = sqlite3.connect("C:/vinicius/sqlite/projeto_sqlite/bd_aeroporto.db")

while True:
    os.system('cls')  # Limpa a tela no Windows
    print('+----------------+')
    print('+    BEM-VINDO   +')
    print('+----------------+')
    print(' 1 - Exibir')
    print(' 2 - Adicionar')
    print(' 3 - Atualizar')
    print(' 4 - Apagar')
    print(' 5 - Finalizar')
    print('+----------------+')

    # Solicita ao usuário a opção
    opcao = input('Opção escolhida: ')

    # Verifica a opção escolhida
    if opcao == '5':  # Finalizar
        print('+----------------+')
        print('Programa finalizado')
        print('+----------------+')
        break

    elif opcao == '1':  # Exibir dados
        tabela = input('Digite o nome da tabela para exibir: ')
        exibir = Exibir()
        exibir.exibir(tabela)

    elif opcao == '2':  # Adicionar dados
        tabela = input('Digite o nome da tabela para adicionar dados: ')
        adicionar = Adicionar()
        adicionar.adicionar(tabela)

    elif opcao == '3':  # Atualizar dados
        tabela = input('Digite o nome da tabela para atualizar dados: ')
        identificador = input('Digite o identificador (ex: cpf ou id): ')
        valor = input(f'Digite o valor do {identificador} para atualizar: ')
        atualizar = Atualizar()
        atualizar.atualizar(tabela, identificador, valor)

    elif opcao == '4':  # Apagar dados
        tabela = input('Digite o nome da tabela para apagar dados: ')
        identificador = input('Digite o identificador (ex: cpf ou id): ')
        valor = input(f'Digite o valor do {identificador} para apagar: ')
        apagar = Apagar()
        apagar.apagar(tabela, identificador, valor)

    else:
        print('Opção inválida. Tente novamente.')

