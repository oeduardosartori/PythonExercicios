"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""
numero = int(input('Digite um número: '))
total = 0
for count in range(1, numero + 1):
    if numero % count == 0:
        print('\033[1;33m', end =' ')
        total += 1
    else:
        print('\033[1;31m', end =' ')
    print(f'{count}', end = " ")
print(f'\n\033[mO número {numero} foi dividido {total} vezes')
if total == 2:
    print(f'O número {numero} é um \033[1;34mNÚMERO PRIMO')
else:
    print(f'O número {numero} \033[1;31mNÃO É PRIMO')
