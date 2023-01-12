"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A médida de idade do grupo;
- Qual é o homem mais velho;
- Quantas mulheres têm menos de 20 anos.
"""
# Dados
soma_idade = 0
media_idade = 0
maior_idade_homem = 0
homem_mais_velho = ''
mulheres_menos_20 = 0
nome_mulher_nova = ''
# Condições
for count in range(1, 5):
    print('=' * 5, f'{count}° PESSOA', '=' * 5)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: '))
    soma_idade += idade
    if count == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        homem_mais_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        homem_mais_velho = nome
    if sexo in 'Ff' and idade < 20:
        mulheres_menos_20 += 1

# Fechamento do programa
media_idade = soma_idade / 4
print(f'A média de idade do grupo é de {media_idade}')
print(f'O nome do homem mais velho é {homem_mais_velho} ele possui {maior_idade_homem} anos.')
print(f'Possuem {mulheres_menos_20} mulheres com menos de 20 anos.')
