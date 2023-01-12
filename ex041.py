"""A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:
- Até 9 anos: Mirim
- Até 14 anos: Infantil
- Até 19 anos: Junior
- Até 20 anos: Sênior
- Acima: Master"""
from datetime import date
current_year = date.today().year
birth = int(input('What year were you born: '))
age = current_year - birth

print(f'You are {age} years old.')
if age <= 9:
    print('Your category is Child! Up to 9 years.')
elif age <= 14:
    print('Your category is Children! Up to 14 years.')
elif age <= 19:
    print('Your category is Junior! Up to 19 years.')
elif age <= 20:
    print('Your category is Senior! Up to 20 years.')
else:
    print('Your category is Master! Over 20 years')
