"""
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a
ser cadastrado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.
"""
print('=' * 20)
print('->BANCO BRASILEIRO<-')
print('=' * 20)
valor = int(input("Que valor você deseja sacar? R$ "))
print('=' * 20)
total = valor
cedulas = 100
total_cedulas = 0
while True:
    if total >= cedulas:
        total -= cedulas
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f'Total de {total_cedulas} cédulas de R$ {cedulas}')
        if cedulas == 100:
            cedulas = 50
        elif cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        total_cedulas = 0
        if total == 0:
            break
print('=' * 20)
print(f'Saque de R$ {valor:.2f} efetuado com sucesso.\nVOLTE SEMPRE!')
