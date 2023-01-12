#O professor quer sortear um de seus 4 alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles
#... e escrevendo o nome do escolhido.
from random import choice
aluno01 = str(input('Nome do primeiro aluno: '))
aluno02 = str(input('Nome do segundo aluno: '))
aluno03 = str(input('Nome do terceiro aluno: '))
aluno04 = str(input('Nome do quarto aluno: '))
sorteio = choice([aluno01, aluno02, aluno03, aluno04])
print(f'O aluno sorteado para apagar o quadro foi {sorteio}.')
