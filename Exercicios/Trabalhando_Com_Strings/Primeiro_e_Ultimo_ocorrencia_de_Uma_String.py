# Ex026-Primeira e última ocorrência de uma string REVER#
print('{:=^40}'.format('Ex026'))

name = (str(input('Digite uma frase qualquer: ')).strip()).upper()

print('Tem {} letras A na frase'.format(name.count('A')))
print('A primeira letra A aparece na {} posição'.format(name.find('A') + 1))
print('A última letra A aparece na {} posição'.format(name.rfind('A') + 1))