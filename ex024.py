#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
nome_da_cidade = str(input('Infome o nome da cidade em que você mora: ')).strip()
print(f'A cidade {nome_da_cidade} começa com SANTO?')
print(nome_da_cidade[:5].upper() == 'SANTO')
