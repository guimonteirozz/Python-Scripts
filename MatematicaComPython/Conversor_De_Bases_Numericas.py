numeroInt = int(input('Digite um número inteiro: '))

print('''Escolha uma da opações de conversao: 
1-para-Binário
2-para-Octadecimal
3-para-Hexadecimal''')
escolher = int(input('Digite aqui sua escolha: '))

if escolher == 1:
    print("{} em Binario é = {}".format(numeroInt,bin(numeroInt)[2:]))
elif escolher == 2:
    print("{} em Octadecimal é = {}".format(numeroInt,oct(numeroInt)[2:]))
elif escolher == 3:
    print("{} em Hexadecimal é = {}".format(numeroInt,hex(numeroInt)[2:]))
else:
    print("opção invalida, tente novamente")