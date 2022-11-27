# Ex022-Analisador de texto REVER#
print('{:=^40}'.format('Ex022'))

nome = input('Digite seu nome completo: ')

print('Seu nome em Maiusculas é = {}'.format(nome.upper()))
print('Seu nome em Minúsculas é = {}'.format(nome.lower()))

# conta as caracteres tiras os esapaças na ponta e tira os espaços no meio #
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))

# retorne a quantidade que tem no primario espaço #
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))