"""Faça um programa que calcule a soma entre todos os números ímpares que são multiplos de três e que se encontram
no intervalo de 1 até 500"""
soma = 0
contador = 0
for impar in range(3, 501, 2):
    if impar % 3 == 0:
        contador += 1
        soma += impar
print(f'A soma de todos os {contador} valores solicitados é {soma}')
