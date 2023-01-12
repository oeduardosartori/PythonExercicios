"""
Crie um programa que tenha Tuplas totalmente preenchidas com uma contagem por extenso de zero até vinte.
Seu programa deverá ler um número pelo telcado (entre 0 - 20) e mostra-lo por extenso.
"""
numeros = 'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', \
          'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezeseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte'
digito = int(input('Digite um número entre 0 e 20: '))
if digito < 0 or digito > 20:
    novo = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    while True:
        if novo < 0 or novo > 20:
            novo = int(input('Tente novamente. Digite um número entre 0 e 20: '))
        else:
            print(f'Você digitou o número {numeros[novo]}')
            break
else:
    print(f'Você digitou o número {numeros[digito]}')
