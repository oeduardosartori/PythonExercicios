"""
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média e o menor dos
valores lidos. O programa deve perguntar ao usuário se ele quer ou não cotinuar a digitar valores.
"""
numero = soma = contador = maior = menor = 0
resposta = 'S'
while resposta != 'N':
    numero = int(input('Digite um número: '))
    resposta = str(input('Deseja continuar digitando valores [S/N]? ')).strip().upper()[0]
    soma += numero
    contador += 1
    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
print('Chegamos ao final.')
print(f'Você digitou {contador} números e a média entre eles foi de {soma / contador:.1f}!')
print(f'O menor número digitado foi {menor} e o maior foi {maior}')
