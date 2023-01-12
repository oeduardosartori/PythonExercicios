"""
Crie um programa que leia dois valores e mostre um menu na tela?
[1] soma
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicidata em cada caso.
"""

#CORES
bold = '\033[1m'
azul = '\033[1;34m'
azul_bg = '\033[1;30;44m'
verde = '\033[1;32m'
verde_bg = '\033[1;30;42m'
preto = '\033[1;37;40m'
clear = '\033[m'
#DADOS
v1 = int(input('Digite o 1° valor: '))
v2 = int(input('Digite o 2° valor: '))
usuario = 0
while usuario != 5:
    print(f'{azul_bg}Esolha uma opção:{clear}')
    print(f'{azul}[1] soma\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa{clear}')
    usuario = int(input(f'{bold}Escolha uma opção:{clear} '))
    if usuario == 1:
        print(f'{verde_bg}Você escolheu SOMA.{clear}')
        print(f'{bold}A soma de{clear} {verde}{v1}{clear} {bold}mais{clear} {verde}{v2}{clear} {bold}é igual a:{clear} {verde}{v1 + v2}{clear}')
    elif usuario == 2:
        print(f'{verde_bg}Você escolheu MULTIPLICAR.{clear}')
        print(f'{bold}A multiplicação entre{clear} {verde}{v1}{clear} {bold}e{clear} {verde}{v2}{clear} {bold}é igual a:{clear} {verde}{v1 * v2}{clear}')
    elif usuario == 3:
        print(f'{verde_bg}Você escolheu o número maior.{clear}')
        if v1 > v2:
            print(f'{bold}O valor maior é o{clear} {verde}{v1}{clear}')
        elif v2 > v1:
            print(f'{bold}O valor maior é o{clear} {verde}{v2}{clear}')
        else:
            print(f'{bold}Os dois valores são iguais.{clear}')
    elif usuario == 4:
        print(f'{verde_bg}Você escolheu digitar novos números!{clear}\n{verde_bg}Pode digitar novamente dois números.{clear}')
        v1 = int(input(f'{verde}Digite o 1° valor: '))
        v2 = int(input(f'{azul}Digite o 2° valor: '))
print(f'{preto}PROGRAMA ENCERRADO!{clear}')
