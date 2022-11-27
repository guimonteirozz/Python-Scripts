c = ' '

while c not in 'MF':
    c = str(input("Digite seu sexo[M/F]: ")).upper()
    
    if c not in 'MF':
        print("Valor invalido Tente Novamente")

print('Valor correto')
