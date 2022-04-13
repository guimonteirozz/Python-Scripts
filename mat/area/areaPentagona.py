from cmath import tan
from math import radians

ladoPent = float(input("Tamanho dos lados: "))

areaFinal = ladoPent * (ladoPent*ladoPent) / (4*tan(radians(36)))

print("{} x {}² / 4 x tangente de 36º = {}".format(ladoPent,ladoPent,areaFinal))
