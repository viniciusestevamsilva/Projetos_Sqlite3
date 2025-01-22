import os
import sqlite3
import time

conn = sqlite3.connect("C:/vinicius/sqlite/exercicio_sql/viagens.db")
conn.execute("PRAGMA foreign_keys = ON;")
cursor = conn.cursor()

tabelas = {
    
    '1':('passageiro',  ['nome','CPf','data_de_nascimento','classe','assento']),
    
    '2':('minha_passagens', ['id_passageiro','preco','duracao_viagem','data_viagem','origem_destino']),
    
    '3':('voos',    ['origem_destino','status_voo','passagens_disponiveis','preco_passagem','companhia_responsavel']),
    
    '4':('companhias',  ['nome_companhia','numero_voo','avaliacao','aviao','capacidade'])
           
           }

while True:
    
    os.system('cls') 
    print('+-----------------+')

    print('+-----------------+')
    print('| 1 - Exibir      |')
    print('| 2 - Adicionar   |')
    print('| 3 - Atualizar   |')
    print('| 4 - Apagar      |')
    print('| 5 - Finalizar   |')
    print('+-----------------+')

    opcao = input('Opção escolhida: ')