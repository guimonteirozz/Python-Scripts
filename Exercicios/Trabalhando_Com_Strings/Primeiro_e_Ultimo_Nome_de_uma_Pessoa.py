# Ex027-Primeiro e ultimo nome de uma pessoa REVER #
print('{:=^40}'.format('Ex027'))

pessoa = str(input('Digite seu nome completo: ')).strip().split()

print('Seu primeiro nome é {}'.format(pessoa[0]))
print('Seu último nome é {}'.format(pessoa[len(pessoa) - 1]))
