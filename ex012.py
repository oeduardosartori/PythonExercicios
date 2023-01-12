# Faça um algoritmo que leia o preço do produto e mostre seu novo preço com 5% de desconto.
valor = float(input('Informe o preço do produto: R$ '))
desconto = valor * 0.05
print(f'O preço deste produto com 5% de desconto fica R$ {valor - desconto:.2f}')
