"""Faça um programa que leia o ano de nascimento de um jovem e informa, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora se é a hora de se alistar.
- Se já passou o tempo de alistamento.
Seu programa também deverá mostrar o tempo que falta ou passou do prazo."""

from datetime import date
nascimento = int(input('Informe seu ano de nascimento: '))
atual = date.today().year
idade_atual = atual - nascimento
alistamento = 18
if idade_atual < alistamento:
    print(f'Quem nasceu em {nascimento} tem {2022 - nascimento} anos em {atual}')
    print(f'Ainda faltam {alistamento - idade_atual} anos para seu alistameneto')
    print(f'O ano para você se alistar sera em {alistamento - idade_atual + atual}')
elif idade_atual > alistamento:
    print(f'Quem nasceu em {nascimento} tem {atual - nascimento} anos em {atual}')
    print(f'Já passou {idade_atual - alistamento} anos da data de prazo para seu alistamento')
    print(f'Seu ano de alistamento foi {atual - (idade_atual - alistamento)}')
else:
    print(f'Quem nasceu em {nascimento} tem {atual - nascimento} anos em {atual}')
    print(f'Esta na hora de se alistar')
