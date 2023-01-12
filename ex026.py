#Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).strip().lower()
quantidade = frase.count('a')
primeira = frase.find('a') + 1
ultima = frase.rfind('a') + 1
print(f'Na frase {frase} aparece')
print(f'{quantidade} vezes a letra A')
print(f'A primeira letra A apareceu na posição {primeira}')
print(f'A última letra A apareceu na posição {ultima}')
