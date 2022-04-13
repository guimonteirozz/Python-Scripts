print("0 - Raio")
print("1 - Diâmetro")
formula = int(input("Selecione uma fórmula, se é pelo Raio ou pelo Diâmetro: "))

if formula == 0:
    raio = float(input("Digite o raio: "))

    areaFinal =  3.1415 * (raio*raio)

    print("Area do circulo pelo Raio π x {}² = {}m²".format(raio,areaFinal))
elif formula == 1:
    diamatro = float(input("Digite o diamêtro: "))

    areaFinal = 3.1415 * (diamatro*diamatro)/4

    print("Area do circulo pelo Diamêtro π x {}² / 4 = {}m²".format(diamatro,areaFinal))
else:
    print("opção invalida")



