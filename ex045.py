"""Crie um programa que faça o computador jogar jokenpô com você."""
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
game = randint(0, 2)
print('SUAS OPÇÕES PARA JOGAR:')
print('[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA')
player = int(input('Qual é sua jogada? '))
if player > 2:
    print('\033[1;41mJOGADA INVÁLIDA!!!\033[m\n\033[1;41mESCOLHA UMA DAS OPÇÕES ACIMA.\033[m')
else:
    print('=' * 7, '\033[1;32mJOKENPÔ\033[m', '=' * 7)
    print(f'\033[1;35mCOMPUTADOR JOGOU:\033[m \033[1;33m{itens[game]}\033[m\n\033[1;34mVOCÊ JOGOU:\033[m \033[1;33m{itens[player]}\033[m')
    print('=' * 24)

if game == 0: #Game jogou PEDRA
    if player == 0:
        print('\033[1;33mEMPATAMOS.')
    elif player == 1:
        print('\033[1;32mVOCÊ VENCEU!')
    elif player == 2:
        print('\033[1;31mVOCÊ PERDEU!')
elif game == 1: #Game jogou PAPEL
    if player == 0:
        print('\033[1;31mVOCÊ PERDEU!')
    elif player == 1:
        print('\033[1;33mEMPATAMOS.')
    elif player == 2:
        print('\033[1;32mVOCÊ VENCEU!')
elif game == 2: #Game jogou TESOURA
    if player == 0:
        print('\033[1;32mVOCÊ VENCEU!')
    elif player == 1:
        print('\033[1;31mVOCÊ PERDEU!')
    elif player == 2:
        print('\033[1;33mEMPATAMOS.')
