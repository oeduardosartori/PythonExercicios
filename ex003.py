n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
azul = '\033[1:34m'
verde = '\033[4:32m'
fecha = '\033[m'
print(f'A soma de {azul}{n1}{fecha} mais {azul}{n2}{fecha} é {verde}{n1 + n2}{fecha}!')
