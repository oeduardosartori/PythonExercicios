# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario_atual = float(input('Informe seu salário atual: R$ '))
aumento = 0.15 * salario_atual
print(f'Seu salário era de R$ {salario_atual:.2f}, mas você recebeu um aumento de 15% e agora vai receber R$ {salario_atual + aumento:.2f}')
