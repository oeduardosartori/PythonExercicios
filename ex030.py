'''Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.'''
numero = int(input('Digite um número inteiro: '))
resultado = numero % 2
par = resultado == 0

if par:
    print(f'O número {numero} é PAR!')
else:
    print(f'O número {numero} é ÍMPAR!')
