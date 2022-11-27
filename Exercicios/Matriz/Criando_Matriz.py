numero_de_linhas = int(input('Numero de linhas'))

linha = [0] * numero_de_linhas

matriz = [linha] * numero_de_linhas

for l in range(numero_de_linhas):
    linha = []
    for c in range(numero_de_linhas):
        numero = int(
            input(f"Value of [{l},{c}]:"))
        linha.append(numero)
    matriz[l] = linha

for i in range(numero_de_linhas):
    print(matriz[i])
    
