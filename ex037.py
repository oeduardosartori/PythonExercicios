"""Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de converção.
- 1 para binário - 2 para octal - 3 para hexadecimal"""
numero = int(input('Digite um número inteiro: '))
print("""Escolha uma das bases para converção:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL""")
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'{numero} convertido para BINÁRIO é igual a {bin(numero)}')
elif opcao == 2:
    print(f'{numero} convertido para OCTAL é igual a {oct(numero)}')
elif opcao == 3:
    print(f'{numero} convertido para HEXADECIMAL é igual a {hex(numero)}')
else:
    print('Esta opção não é valida. \nIndique um número entre 1, 2 ou 3 que corresponda as opções acima!')
