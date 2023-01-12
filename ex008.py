# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
metro = float(input('Uma distância em metros: '))
print(f'A medida de {metro}m corresponde a {int(metro * 100)}cm e {int(metro * 1000)}mm')
