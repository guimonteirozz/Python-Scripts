from time import sleep # Ex 046

print("Os fogos vão estourar em..")

for i in range (10,-1,-1):
    print(i)
    sleep(1)
print("**BOOOOOOOO**")

# ================================ #
print("-=" * 20) # Ex 047

for a in range (2,51,2):
    print('.',end='')
    print(a, end='')
print(" acabou")

# ================================ #
print("-=" * 20) # Ex 048
soma = 0
cont = 0
for q in range (1,501,2):
    if q % 3 == 0: 
        cont += 1
        soma += q

print('A soma dos {} valores solicitados é {}'.format(cont,soma))

# ================================ #
print("-=" * 20) # Ex 049

numb = int(input("Digite o numero para a tabuada: "))
print("=====Tabuada do {}=====".format(numb))
for c in range (1,11):
    produto = numb * c
    print("{} x {} = {}".format(numb, c,produto))

# ================================ #
print("-=" * 20) # Ex 050
mais = 0
contador = 0
for s in range (1,7):
    numb = int(input("Digite {}º valor: ".format(s)))
    if numb%2 == 0:
        mais += numb
        contador += 1
print("Voce informal {} pares e sua Soma é = {}".format(contador,mais)) 

