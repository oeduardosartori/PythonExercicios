"""Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
para os inferiores ou iguais, o aumento é de 15%."""

salario = float(input('Informe o seu salário: R$ '))
if salario > 1250:
    aumento = salario * 0.10 + salario
    print(f'Seu salário de R$ {salario:.2f} aumentou para R$ {aumento:.2f}')
else:
    aumento = salario * 0.15 + salario
    print(f'Seu salário de R$ {salario:.2f} aumentou para R$ {aumento:.2f}')
