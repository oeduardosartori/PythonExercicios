"""Reforça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo sera formado:
- Equilátero: Todos os lados iguais
- Isóceles: Dois lados iguais
- Escaleno: Todos os lados diferentes"""
# cores
blue = '\033[34m'
green = '\033[32m'
red = '\033[31m'
back_red = '\033[7;31;40m'
clear = '\033[m'
# info
print('Analisando seu triângulo')
print('=' * 20)
# Dados necessários
r1 = float(input('Digite o 1° segmento: '))
r2 = float(input('Digite o 2° segmento: '))
r3 = float(input('Digite o 3° segmento: '))
# Condições
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo:')
    if r1 == r2 and r2 == r3:
        print(f'{green}EQUILÁTERO{clear}')
    elif r1 == r2 or r1 == r3 or r3 == r2:
        print(f'{red}ISÓCELES{clear}')
    else:
        print(f'{blue}ESCALENO{clear}')
else:
    print(f'{back_red}Os segmentos acima não podem formar um triângulo!{clear}')
