"""
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando
o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
from random import randint

print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR!?')
print('=-' * 15)
vitoria = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar [P/I]? ')).strip().upper()[0]
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU!')
            print(f'Você jogou {jogador} e o computador jogou {computador}. Total foi {total} DEU PAR.')
            vitoria += 1
        else:
            print('VOCÊ PERDEU')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCÊ VENCEU!')
            print(f'Você jogou {jogador} e o computador jogou {computador}. Total foi {total} DEU ÍMPAR.')
            vitoria += 1
        else:
            print('VOCÊ PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {vitoria} vezes ')
