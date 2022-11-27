# Ex019-Sorteando um item na lista #
from random import choice
print('{:=^40}'.format('Ex019-Sorteando um item na lista'))

aluno1 = input('Digite o nome do Primeiro Aluno: ')
aluno2 = input('Digite o nome do Segundo Aluno: ')
aluno3 = input('Digite o nome do Terceiro Aluno: ')
aluno4 = input('Digite o nome do Quarto Aluno: ')

listaDeAlunos = [aluno4, aluno3, aluno2, aluno1]

print(f'Aluno sorteado é {choice(listaDeAlunos)}')