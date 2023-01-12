#Faça um programa que leia o comprimento do cateto oposto e do triângulo retângulo, calcule e mostre o comprimento
#...da hipotenusa.
from math import hypot
oposto = float(input('Qual o comprimento do cateto oposto? '))
adjacente = float(input('Qual o comprimento do cateto adjacente? '))
hi = hypot(oposto, adjacente)
print(f'A hipotenusa vai medir {hi:.2f}')
