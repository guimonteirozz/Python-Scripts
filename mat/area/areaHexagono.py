# PARA PENTAGONOS DE LADOS IGUAIS #
from math import sqrt

ladoHex = float(input("Tamanho dos lados: "))

areaFinal = (3 * (ladoHex*ladoHex) * sqrt(3)) / 2

print("Area do hexagono 3 x {}² x raiz de 3 / 2 = {}m²".format(ladoHex,areaFinal))