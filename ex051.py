"""
Desenvolva um programa que leia o 1° termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
"""
print('=' * 25)
print('  10 TERMOS DE UMA PA')
print('=' * 25)
termo1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo1 + (10 - 1) * razao
for pa in range(termo1, decimo + 1, razao):
    print(f'{pa}', end=' -> ')
print('ACABOU!')
