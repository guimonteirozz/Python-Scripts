# Sorteando uma ordem na lista #
from random import shuffle
print('{:=^40}'.format('Ex020-Sorteando uma ordem na lista'))

nome1 = input('Digite o nome do Primeiro Aluno: ')
nome2 = input('Digite o nome do Segundo Aluno: ')
nome3 = input('Digite o nome do Terceiro Aluno: ')
nome4 = input('Digite o nome do Quarto Aluno: ')

nomes = [nome4, nome3, nome2, nome1]
shuffle(nomes)

print(f'A Ordem da apresentação será de {nomes}')
