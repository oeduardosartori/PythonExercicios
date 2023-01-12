# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira.
# Ex: Digite um número: 6.127 = O número 6.127 tem a parte inteira 6.

from math import trunc # A função trunc é usada para arredondar para cima ou para baixo em direção a zero.
num = float(input('Digite um número real: '))
print(f'O número real digitado foi {num} tem a parte inteira {trunc(num)}')
