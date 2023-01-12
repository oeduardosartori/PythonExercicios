"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
maioridade e quantas já são maiores.
"""
from datetime import date
ano = date.today().year
maior = 0
menor = 0
for count in range(1,8):
    nascimento = int(input(f'Em que ano nasceu a {count}° pessoa? '))
    idade = ano - nascimento
    if idade < 18:
        menor += 1
    else:
        maior += 1
print(f'Temos {maior} pessoas menores de idade')
print(f'E também temos {menor} pessoas maiores de idade.')
