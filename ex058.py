"""
Melhore o jogo do DESAFIO 028 onde o computador vai "PENSAR" um número entre 0 a 10. Só que agora tenta adivinhar até
acertar, mostrando no final quantos palpites foram necessários para vencer.
"""

from random import randint

numero_aleatorio = randint(0, 10)
acertou = False
palpites = 0

print('Sou seu computador...\nAcabei de pensar em um número entre 0 e 10\nSerá que você consegue adivinhar qual foi?')
while acertou == False:
    chute = int(input('Qual seu palpite: '))
    palpites += 1
    if chute > numero_aleatorio:
        print('Seu palpite maior que o número pensado. Tente novamente!')
    elif chute < numero_aleatorio:
        print('Seu palpite é menor que o número pensado. Tente novamente!')
    elif chute == numero_aleatorio:
        acertou = True
        print('Parabéns! Você acertou o número que eu pensei.')
print(f'Você precisou de {palpites} palpites para acertar o número.')
