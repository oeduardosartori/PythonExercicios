#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# EX: Ana Maria de Souza
# primeiro nome: Ana
# Último nome: Souza
nome = str(input('Digite seu nome aqui: ')).strip()
primeiro = nome.split()
ultimo = primeiro[len(primeiro) - 1]
print(f'Seu primeiro nome é {primeiro[0]} \n'
      f'seu último nome é {ultimo}')
