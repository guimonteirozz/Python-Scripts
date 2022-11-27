mais = 0
contador = 0

for s in range (1,7):
    
    numb = int(input("Digite {}º valor: ".format(s)))

    if numb%2 == 0:
        mais += numb
        contador += 1

print("Voce informal {} pares e sua Soma é = {}".format(contador, mais)) 