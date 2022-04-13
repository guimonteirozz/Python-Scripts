# ==============================Ex042============================== #
print('{:=^40}'.format("Ex042"))

ladoTriangulo1 = float(input("Digite o lado 1 do triangulo: "))
ladoTriangulo2 = float(input("Digite o lado 2 do triangulo: "))
ladoTriangulo3 = float(input("Digite o lado 3 do triangulo: "))

if ladoTriangulo1 < ladoTriangulo2 + ladoTriangulo3 and ladoTriangulo2 < ladoTriangulo1 + ladoTriangulo3 and ladoTriangulo3 < ladoTriangulo1 + ladoTriangulo2:
    print("Pode ser trinagulo")
    if ladoTriangulo1 == ladoTriangulo2 == ladoTriangulo3:
        print("É um triangulo EQUILATERO")
    if ladoTriangulo1 != ladoTriangulo2 != ladoTriangulo3 != ladoTriangulo1:
        print("É um triangulo ESCALENO") 
    else:
        print("É um triangulo ISÓSCELES")     
else:
    print('Nao pode ser triangulo')