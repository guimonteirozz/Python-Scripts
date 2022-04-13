# Aula09-Manipulando Texto #

# Ex022-Analisador de texto REVER#
print('{:=^40}'.format('Ex022'))
nome = input('Digite seu nome completo: ')
print('Seu nome em Maiusculas é = {}'.format(nome.upper()))
print('Seu nome em Minúsculas é = {}'.format(nome.lower()))
# conta as caracteres tiras os esapaças na ponta e tira os espaços no meio #
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
# retorne a quantidade que tem no primario espaço #
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

# Ex023-Separando dígitos de um número REVER #
print('{:=^40}'.format('Ex023'))
num = int(input('Digite um Número de 0 a 9999: '))
print('Analisando o número {}'.format(num))
print('{} Unidades'.format(num // 1 % 10)) # pega o valor de num divide pr 1 e tira o modulo com 10 #
print('{} Dezenas'.format(num // 10 % 10))
print('{} Centenas'.format(num // 100 % 10))
print('{} Milhar'.format(num // 1000 % 10))

# Ex024-Verificando as primeiras letras de um texto REVER #
print('{:=^40}'.format('Ex024'))
cidade = str(input('Qual cidade você nasceu ')).strip()
print(cidade[:5].upper() == 'SANTO')

# Ex025-Procurando uma string dentro da outra REVER #
print('{:=^40}'.format('Ex025'))
nomesilva = str(input("Qual seu nome completo: ")).strip()
print('Seu nome tem Silva? {}'.format('silva' in nomesilva.lower()))

# Ex026-Primeira e última ocorrência de uma string REVER#
print('{:=^40}'.format('Ex026'))
name = (str(input('Digite uma frase qualquer: ')).strip()).upper()
print('Tem {} letras A na frase'.format(name.count('A')))
print('A primeira letra A aparece na {} posição'.format(name.find('A') + 1))
print('A última letra A aparece na {} posição'.format(name.rfind('A') + 1))

# Ex027-Primeiro e ultimo nome de uma pessoa REVER #
print('{:=^40}'.format('Ex027'))
pessoa = str(input('Digite seu nome completo: ')).strip().split()
print('Seu primeiro nome é {}'.format(pessoa[0]))
print('Seu último nome é {}'.format(pessoa[len(pessoa) - 1]))
