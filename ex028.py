'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 a 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo computador.
O programa deve escrever na tela se o usuário venceu ou perdeu!'''

import random

valor_aleatorio = random.randint(0, 5)
acertou = False
while acertou == False:
    chute = int(input('Chute um número de 0 a 5: '))
    if chute > valor_aleatorio:
        print('Seu chute foi maior que o valor gerado. \n Tente novamente!')
    elif chute < valor_aleatorio:
        print('Seu chute foi menor que o valor gerado. \n Tente novamente!')
    else:
        acertou == True
        print('Você venceu o jogo. \n Parabéns!')
