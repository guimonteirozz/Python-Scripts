#Ex008 Converso de medidas

print("{:=^40}".format('Ex008-Conversor de Medidas'))

metro = int(input('Digite um Valor em Metros: '))

print(f'Valor em Quilômetro = {metro * 0.001} km')
print(f'Valor em Hectômetro = {metro * 0.01} hm')
print(f'Valor em Decâmetro = {metro * 0.1} dam')
print(f'Valor em Metro = {metro} m')
print(f'Valor em Decímentro = {metro * 10} dm')
print(f'Valor em Centímetros = {metro * 100} cm')
print(f'Valor em Milímetros = {metro * 1000} mm')