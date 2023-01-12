"""
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
"""

while True:
    print('-' * 20)
    numero = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 20)
    if numero < 0:
        break
    for tabuada in range(1, 11):
        print(f'{numero} X {tabuada} = {numero * tabuada}')
print('PROGRAMA TABUADA ENCERRADO.')
