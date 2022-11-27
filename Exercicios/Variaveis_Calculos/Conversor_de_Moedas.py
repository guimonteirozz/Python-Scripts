#Ex010 Conversor de Moedas
print('{:=^40}'.format('Ex010-Conversor de Moedas'))

moeda = float(input('Digite o valor EM REAL, para saber quantos dolares você pode comprar: '))

print('Você pode comprar {:.2f} dólares'.format(moeda / 3.27)) #pegar o cotação atual do dolar