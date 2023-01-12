"""
Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de
Fibonacci.  EX -> 0 - 1 - 1 - 2 - 3 - 5 - 8
"""
print('SEQUÊNCIA DE FIBONACCI')
print('=' * 20)
numero = int(input('Quantos termos você deseja ver? '))
t1 = 0
t2 = 1
print('~' * 20)
print(f'{t1} -> {t2}', end="")
contador = 3
while contador <= numero:
    t3 = t1 + t2
    print(f' -> {t3}', end="")
    contador += 1
    t1 = t2
    t2 = t3
print('-> FIM')
