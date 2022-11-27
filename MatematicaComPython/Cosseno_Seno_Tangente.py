#Ex018-Seno,Cosseno e Tangente 
from math import sin, cos, tan, radians
print('{:=^40}'.format('Ex018-Seno,Cosseno e Tangente'))

angulo = float(input('Digite o valor do ângulo: '))

print('O Seno de {} é = {:.2f}'.format(angulo, sin(radians(angulo))))
print('O Cosseno de {} é = {:.2f}'.format(angulo, cos(radians(angulo))))
print('A Tangente de {} é = {:.2f}'.format(angulo, tan(radians(angulo))))