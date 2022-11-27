#Ex017-Catetos e Hipotenusa #
import math
print('{:=^40}'.format('Ex017-Catetos e Hipotenusa'))

co = float(input('Digite o valor do CATETO OPOSTO: '))
ca = float(input("Digite o valor do CATETO ADJACENTE: "))

# Calculo da Hipotenusa ou Função da hipotenusa #
print('O valor da HIPOTENUSA é = {:.2f}'.format(math.hypot(co, ca)))