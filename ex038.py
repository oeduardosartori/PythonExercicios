"""Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais"""

numero01 = int(input('Digite um núnero inteiro: '))
numero02 = int(input('Digite mais um número inteiro: '))

if numero01 > numero02:
    print('O primeiro número digitado é maior!')
elif numero01 < numero02:
    print('O segundo número digitado é maior!')
else:
    print('Não existe um número maior, os dois são iguais.')
