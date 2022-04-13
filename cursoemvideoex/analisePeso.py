maior = 0
menor = 0
for i in range(1,6):
    peso = float(input("Digite o peso da pessoa {}: ".format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O Maior peso lido é {}'.format(maior))
print('O Menor peso lido é {}'.format(menor))

        
