# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos
#...quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

km_percorridos = float(input('Quantos km você percorreu com o carro alugado? '))
dias_alugados = int(input('Quantos dias você locou o carro? '))
custo_dia = dias_alugados * 60.00
custo_km = km_percorridos * 0.15
valor_aluguel = custo_dia + custo_km

print(f'Olá, valor total a ser pago pelo aluguel do carro é de R$ {valor_aluguel:.2f}')
