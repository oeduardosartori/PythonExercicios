"""
Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
"""

print('GERADOR DE PA')
print('=' * 20)
primeiro_termo = int(input('1° termo: '))
razao = int(input('Razão: '))
termo = primeiro_termo
contador = 1
total = 0
mais = 10
while mais != 0:
    total += mais

    while contador <= total:
        print(f'{termo} -> ', end= '')
        termo += razao
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos você deseja mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados!')
