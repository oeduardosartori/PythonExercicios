"""
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
"""
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

""" inverso = ''
for letra in range(len(junto) - 1, - 1, - 1):
    inverso += junto[letra]"""

print('\033[1;34m', junto, inverso, '\033[m')
if inverso == junto:
    print(f'A frase \033[4m{frase}\033[m é um \033[1;33mPALÍNDROMO\033[m')
else:
    print(f'A frase \033[4m{frase}\033[m \033[1;31mNÃO É PALÍNDROMO\033[m')
