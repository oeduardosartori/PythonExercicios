"""
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor dividido for ímpar, desconsidere-o
"""
soma = 0
contador = 0
for c in range(1,7):
    numero = int(input(f'Digite o {c}° número: '))
    if numero % 2 == 0:
        soma += numero
        contador += 1
print(f'A soma dos {contador} números pares são {soma}')
