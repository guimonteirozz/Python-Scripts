soma = 0
nomeHomemVelho = ''
maiorIdadeHomem = 0
cont = 0
for i in range (1,5):
    print('==========PESSOA {}=========='.format(i))
    nome = input('NOME: ').capitalize().strip()
    idade = int(input('IDADE: '))
    sexo = input('SEXO[M/F]: ').upper().strip()

    soma += idade

    if sexo in 'M' and i == 1:
        maiorIdadeHomem = idade
        nomeHomemVelho = nome
    if sexo in 'M' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeHomemVelho = nome

    if sexo in 'F':
        if idade < 20:
            cont += 1
  
mediaIdade = soma/4

print('A Media das idades é {}'.format(mediaIdade))
print('O Homem mais velho é {} e tem {} anos'.format(nomeHomemVelho,maiorIdadeHomem))
print('E tem {} mulheres menor de 20 anos'.format(cont))


'''
Desenvolva um programa que leia o nome, idade e sexo de 
4 pessoas. No final do programa, mostre: a média de idade do grupo,
qual é o nome do homem mais velho e quantas 
mulheres têm menos de 20 anos.
'''