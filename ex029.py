'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada Km a cima do limite.'''

velocidade_carro = float(input('Infome a velocidade do seu carro: '))
multa = (velocidade_carro - 80) * 7
if velocidade_carro > 80:
    print(f'Você foi multado! \n O valor da sua multa é de R$ {multa:.2f}!')
else:
    print('Parabéns! Você conseguiu passar sem levar multa.')
