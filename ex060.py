"""
Faça um programa que leia um número qualquer e mostre o seu fatorial.
ex: [5] = 5x4x3x2x1 = 120
"""

numero = int(input('Digite um número para calcular o fatorial: '))
count = numero
fatorial = 1
print(f'Calculando {numero}! =', end=' ')
while count > 0:
    print(f'{count}', end=' ')
    if count > 1:
        print('x', end=' ')
    else:
        print('=', end=' ')
    fatorial *= count
    count -= 1
print(f'{fatorial}')
