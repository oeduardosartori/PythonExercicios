"""
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lido.
"""
maior = 0
menor = 0
for count in range(1, 6):
    peso = float(input(f'Informe o pesso da {count}° pessoa: '))
    if count == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso é {maior:.1f}Kg')
print(f'O menor peso é {menor:.1f}Kg')
