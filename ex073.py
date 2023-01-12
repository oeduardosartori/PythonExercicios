"""
Crie uma Tupla preenchida com os 20 primeiros colocados da tabela do campeonato Brasileiro, na ordem de colocação.
Depois mostre:
a) Apenas os 5 primeiros colocados;
b) Os últimos 4 colocados da tabela;
c) Uma lista com os times em ordem alfabética;
d) Em que posisão da tabela esta o time do Grêmio.
"""
tabela = 'Cruzeiro', 'Grêmio', 'Bahia', 'Vasco', 'Sampaio', 'Ituano', 'Sport', 'Criciuma', 'Londrina', 'Guarani', \
         'CRB', 'Ponte Preta', 'Vila Nova', 'Chapecoense', 'Tombense', 'Novorizontino', 'CSA', 'Brusque', 'Operario', 'Nautico'
print('TABELA BRASILEIRÃO SERIE B 2022')
print('=' * 20)
print(f'Times = {tabela}')
print('OS 5 PRIMEIROS COLOCADOS SÃO:')
print(tabela[:5])
print('=' * 20)
print('OS ÚLTIMOS 4 COLOCADOS SÃO:')
print(tabela[16:])
print('=' * 20)
print('TIMES EM ORDEM ALFABÉTICA')
print(sorted(tabela))
print('=' * 20)
print('POSIÇÃO DO GRÊMIO NA TABELA')
#FINALIZARA A ÚLTIMA QUESTÃO
