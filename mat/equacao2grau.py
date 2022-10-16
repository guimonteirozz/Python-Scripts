from math import sqrt

a = float(input("Digite valor de A: "))
b = float(input("Digite valor de B: "))
c = float(input("Digite valor de C: "))

if a != 0:
    delta = (b*b) - 4*(a*c)
    print(f"Delta = {delta}")
    if delta < 0:
        print("Não existe raiz.")
    else:
        x1 = (-b + sqrt(delta)) / (2*a); 
        x2 = (-b - sqrt(delta)) / (2*a);
        if delta == 0:
            print("Raiz Unica/Unica Solução") 
            print(x1)
        else:
            print(f"X1 = {x1}")
            print(f"X2 = {x2}")
else:
    print("Não é equação do segundo grau.")
