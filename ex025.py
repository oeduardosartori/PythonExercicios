#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input('Qual seu nome completo? ')).strip()
silva = 'SILVA' in nome.upper()
print(f'{nome} tem Silva em seu nome? {silva}')
