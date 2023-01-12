#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos.
#Faça um programa que leia o nome dos alunos e mostre a ordem sorteada.
from random import shuffle
student01 = input('Enter the name of the first student: ')
student02 = input('Enter the name of the second student: ')
student03 = input('Enter the name of the third studant: ')
student04 = input('Enter the name of the fourth studant: ')
student05 = input('Enter the name of the fifth studant: ')
list = [student01, student02, student03, student04, student05]
shuffle(list)
print(f'The order drawn for the presentation of the work was as follows: \n {list}')
