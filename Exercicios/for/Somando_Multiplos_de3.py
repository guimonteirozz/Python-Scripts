soma = 0
cont = 0

numeroInicial = 1
numeroFinal = 9

for q in range (numeroInicial, numeroFinal):
    print(q)
    if q % 3 == 0: 
        cont += 1
        soma += q

print('A soma dos {} valores solicitados é {}'.format(cont, soma))

# Soma todos os valores multiplos de 3 1 -> 501
