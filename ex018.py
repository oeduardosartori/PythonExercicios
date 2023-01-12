#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians
angulo = float(input('Digite um ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'Veja abaixo o valor em seno, consseno e tangente do ângulo {angulo}'"\n"
      f'O valor do ângulo {angulo} em seno é de {seno:.2f}''\n'
      f'O valor do ângulo {angulo} em cosseno é de {cosseno:.2f}''\n'
      f'O valor do ângulo {angulo} na tangente é de {tangente:.2f}')
