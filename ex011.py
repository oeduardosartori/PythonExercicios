# Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade
# de tinta necessária para pinta-lá, sabendo que cada litro de tinta, pinta uma área de 2 metros quadrados.
largura_da_parede = float(input('Qual é a largura de sua parede? '))
altura_da_parede = float(input('Qual é a altura de sua parede? '))
print(f'Sua parede tem a dimensão de {largura_da_parede}X{altura_da_parede} e sua área é de {largura_da_parede * altura_da_parede:.2f}m²')
print(f'Para pintar toda sua parede, será necessário {(largura_da_parede * altura_da_parede) / 2:.1f}l de tinta.')
