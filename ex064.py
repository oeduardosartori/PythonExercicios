"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor
999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag)
"""
numeros = contador = soma = 0
numeros = int(input('Digite um número: '))
print('Para parar digite 999!')
while numeros != 999:
    contador += 1
    soma += numeros
    numeros = int(input('Digite um número: '))
    print('Para parar digite 999!')
print(f'Você digitou {contador} números e a soma entre eles foi {soma}.')
