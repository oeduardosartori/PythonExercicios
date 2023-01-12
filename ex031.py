"""Desenvolva um programa que pergunte a distânica de uma viagem em Km.
Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens até 200Km e R$ 0,45 para viagens mais longes."""

distancia = float(input('Digite a distância da sua viagem: '))
valor1 = 0.50
valor2 = 0.45
if distancia < 200:
    print(f'O valor da sua viagem é de R$ {distancia * valor1:.2f}')
else:
    print(f'O valor da sua viagem é de R$ {distancia * valor2:.2f}')
