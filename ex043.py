"""Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com
a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida"""

peso = float(input('Seu peso: '))
altura = float(input('Sua altura: '))
imc = peso / altura ** 2

print(f'Seu IMC é de {imc:.1f}')
if imc < 18.5:
    print('Você está abaixo do seu peso ideal!')
elif imc <= 25:
    print('Parabéns! Você está no seu peso ideal.')
elif imc <= 30:
    print('Você está com sobrepeso!')
elif imc <= 40:
    print('Cuidado! Você esta na obesidade.')
else:
    print('Procure um médico! Você está na obesidade mórbida.')
