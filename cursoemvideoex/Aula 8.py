#Ex016-Quebrando um Número #
print('{:=^40}'.format('Ex016-Quebrando um Número'))
import math
num = float(input('Digite um número real quebrado: '))
print('A parte inteira de {} é = {}'.format(num, math.trunc(num)))

#Ex017-Catetos e Hipotenusa #
print('{:=^40}'.format('Ex017-Catetos e Hipotenusa'))
co = float(input('Digite o valor do CATETO OPOSTO: '))
ca = float(input("Digite o valor do CATETO ADJACENTE: "))
# Calculo da Hipotenusa ou Função da hipotenusa #
print('O valor da HIPOTENUSA é = {:.2f}'.format(math.hypot(co, ca)))

#Ex018-Seno,Cosseno e Tangente #
print('{:=^40}'.format('Ex018-Seno,Cosseno e Tangente'))
angulo = float(input('Digite o valor do ângulo: '))
print('O Seno de {} é = {:.2f}'.format(angulo, math.sin(math.radians(angulo))))
print('O Cosseno de {} é = {:.2f}'.format(angulo, math.cos(math.radians(angulo))))
print('A Tangente de {} é = {:.2f}'.format(angulo, math.tan(math.radians(angulo))))

# Ex019-Sorteando um item na lista #
print('{:=^40}'.format('Ex019-Sorteando um item na lista'))
import random
aluno1 = input('Digite o nome do Primeiro Aluno: ')
aluno2 = input('Digite o nome do Segundo Aluno: ')
aluno3 = input('Digite o nome do Terceiro Aluno: ')
aluno4 = input('Digite o nome do Quarto Aluno: ')
lista = [aluno4, aluno3, aluno2, aluno1]
print('Aluno sorteado é {}'.format(random.choice(lista)))

# Ex020-Sorteando uma ordem na lista #
print('{:=^40}'.format('Ex020-Sorteando uma ordem na lista'))
nome1 = input('Digite o nome do Primeiro Aluno: ')
nome2 = input('Digite o nome do Segundo Aluno: ')
nome3 = input('Digite o nome do Terceiro Aluno: ')
nome4 = input('Digite o nome do Quarto Aluno: ')
nomes = [nome4, nome3, nome2, nome1]
random.shuffle(nomes)
print('A Ordem da apresentação será de', nomes)


