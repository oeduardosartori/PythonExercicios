"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles.
(Desconsiderando o flag)
"""
#Cores:
verde = '\033[1;32m'
amarelo = '\033[1;33m'
azul = '\033[1;34m'
bold = '\033[1m'
clear = '\033[m'
#Dados:
numero = soma = contador = 0
#Desenvolvimento:
while True:
    numero = int(input(f'{azul}Digite um valor:{clear} '))
    if numero != 999:
        print(f'{bold}Caso deseja parar digite{clear} {amarelo}[999]{clear}{bold}!')
    if numero == 999:
        break
    soma += numero
    contador += 1
print(f'{bold}=' * 35)
print(f'{bold}A soma dos{clear} {azul}{contador}{clear} {bold}valores foi de:{clear} {verde}{soma}{clear}{bold}!')
