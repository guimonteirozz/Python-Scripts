print('{:=^40}'.format('Exx033'))

numb1 = int(input('Digite o 1º número: '))
numb2 = int(input('Digite o 2º número: '))
numb3 = int(input('Digite o 3º número: '))

if numb1 < numb2 and numb1 < numb3:
    menor = numb1
if numb2 < numb1 and numb2 < numb3:
    menor = numb2
if numb3 < numb1 and numb3 < numb2:
    menor = numb3
if numb1 < numb2 and numb1 < numb3:
    maior = numb1
if numb2 > numb1 and numb2 > numb3:
    maior = numb2
if numb3 > numb1 and numb3 > numb2:
    maior = numb3

print('Maior número é {}'.format(maior))
print('Menor número é {}'.format(menor))

# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.