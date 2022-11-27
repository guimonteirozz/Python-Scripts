#Separando dígitos de um número REVER #
print('{:=^40}'.format('Ex023'))

num = int(input('Digite um Número de 0 a 9999: '))
print('Analisando o número {}'.format(num))

print('{} Unidades'.format(num // 1 % 10)) # pega o valor de num divide pr 1 e tira o modulo com 10 #
print('{} Dezenas'.format(num // 10 % 10))
print('{} Centenas'.format(num // 100 % 10))
print('{} Milhar'.format(num // 1000 % 10))