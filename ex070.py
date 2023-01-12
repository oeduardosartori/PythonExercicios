"""
Crie um programa que leia o nome dos produtos. O programa deverá perguntar se o usuário vai continuar.
No final mostre:
a) Qual o total gasto na compra;
b) Quantos produtos custam mais de R$ 1000;
c) Qual é o nome do produto mais barato.
"""
print('_-' * 20)
print('START UP STORE SINCE 2023')
print('_-' * 20)
total_gasto = mais_de_mil = barato = contador = 0
produto = ''
while True:
    nome_produto = str(input('Nome do Produto: '))
    preco = float(input('Digite o preço:R$ '))
    contador += 1
    total_gasto += preco
    if preco >= 1000:
        mais_de_mil += 1
    if contador == 1 or preco < barato:
        barato = preco
        produto = nome_produto
    stop = ' '
    while stop not in 'SN':
        stop = str(input('Tem mais alguma compra [S/N]? ')).strip().upper()[0]
    if stop =='N':
        break
print('_-' * 35)
print(f'O valor total da compra ficou R$ {total_gasto:.2f}')
print('_-' * 35)
print(f'Sua compra teve {mais_de_mil} que custaram mais de R$ 1000.00')
print('_-' * 35)
print(f'O produto mais barato foi {produto} e custou R$ {barato:.2f}')
print('_-' * 35)
print('VOLTE SEMPRE JOVEM!')
