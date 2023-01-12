"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se
o usuário quer ou não continuar. No final, mostre:
a) Quantas pessoas tem mais de 18 anos;
b) Quantos homens foram cadastrados;
c) Quantas mulheres tem menos de 20 anos.
"""
mulheres20 = homens = maiores = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    stop = ' '
    if idade >= 18:
        maiores += 1
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        homens += 1
    elif sexo == 'F':
        if idade < 20:
            mulheres20 += 1
    stop = ' '
    while stop not in 'SN':
        stop = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if stop == 'N':
        break
print('=-' * 20)
print(f'{maiores} pessoas cadastradas com mais de 18 anos;')
print(f'Temos {homens} homens cadastrados no sistema;')
print(f'E {mulheres20} mulheres com menos de 20 anos cadastradas no sistema.')
