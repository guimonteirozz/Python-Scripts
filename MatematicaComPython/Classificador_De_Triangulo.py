ladoT1 = float(input("Digite o lado 1 do triangulo: "))
ladoT2 = float(input("Digite o lado 2 do triangulo: "))
ladoT3 = float(input("Digite o lado 3 do triangulo: "))

if ladoT1 < ladoT2 + ladoT3 and ladoT2 < ladoT1 + ladoT3 and ladoT3 < ladoT1 + ladoT2:
    print("====PODE SER UM TRIANGULO====")

    if ladoT1 == ladoT2 == ladoT3:

        print("Triangulo EQUILATERO (3 lados iguas)")
    elif ladoT1 != ladoT2 != ladoT3 != ladoT1:

        print("Triangulo ESCALENO (3 lados diferentes)") 
    else:
        
        print("Triangulo ISÓSCELES (2 lados iguais e 1 diferente)")     
else:
    print("====Não PODE SER UM TRIANGULO====")