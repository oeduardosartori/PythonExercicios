"""Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado."""
# Informações necessárias
valor_casa = float(input('Qual o valor da casa que deseja comprar? R$ '))
salario = float(input('Qual é o valor do seu salário atualmente? R$ '))
anos_pagando = int(input('Em quantos anos deseja pagar pela casa? '))
# Cores de auxílio
verde = '\033[1;32m'
vermelho = '\033[1;31m'
x = '\033[m'
# Dados
valor_mensal = valor_casa / (anos_pagando * 12)
valor_maximo = salario * 0.3
# Condições
print(f'\033[7;33;40mRESPOSTA DO BANCO:{x}')
if valor_mensal > valor_maximo:
    print(f'{vermelho}O empréstimo foi negado{x}. \nInfelizmente o valor é incompatível ao seu salário atual!')
else:
    print(f'Seu empréstimo foi aprovado, você pagará um valor mensal de {verde}R$ {valor_mensal:.2f}{x} por {anos_pagando} anos!')
