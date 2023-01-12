"""Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo
com a média atingida:
- Média abaixo de 5.0: Reprovado
- Média entre 5.0 e 6.9: Recuperação
- Média 7.0 ou superiro: Aprovado"""
# Informações
nota1 = float(input('Informe sua 1° nota: '))
nota2 = float(input('Informe sua 2° nota: '))
media = (nota1 + nota2) / 2
# Cores
red = '\033[1;31m'
green = '\033[1;32m'
yellow = '\033[1;33m'
clear = '\033[m'
# Condições
if media < 5.0:
    print(f'Sua nota média foi {red}{media:.1f}{clear}.')
    print(f'Você foi {red}REPROVADO{clear}!')
elif 7 > media >= 5:
    print(f'Sua nota média foi {yellow}{media:.1f}{clear}.')
    print(f'Você está em {yellow}RECUPERAÇÃO{clear}!')
else:
    print(f'Sua nota média foi {green}{media:.1f}{clear}.')
    print(f'Parabéns, você foi {green}APROVADO{clear}!')
