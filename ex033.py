"""Faça um programa que leia três números e mostre qual é o maior e qual é o menor."""
valor_a = int(input('Digite o 1° número: '))
valor_b = int(input('Digite o 2° número: '))
valor_c= int(input('Digite o 3° número: '))

maior = valor_a
if valor_b > valor_a and valor_b > valor_c:
    maior = valor_b
elif valor_c > valor_a and valor_c > valor_b:
    maior = valor_c

menor = valor_b
if valor_a < valor_b and valor_a < valor_c:
    menor = valor_a
elif valor_c < valor_b and valor_c < valor_a:
    menor = valor_c
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')
