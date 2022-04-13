#Ex014 Conversor de Temperatura
print('{:=^40}'.format('Ex014-Conversor de Temperatura'))
celsius = float(input('Digite a temperatua em °C: '))
print('O valor {}°C em Fahrenheit é = {:.2f}°F'.format(celsius,(celsius * 9/5) + 32))

#Ex015  Aluguel de Carros 60 reais por dia 0,15 por km rodado
print('{:=^40}'.format('Ex015-Aluguel de Carros: '))
caminho = float(input('Quantos km você percorreu por com o carro: '))
dias = int(input('Quantos dias você ficou com o carro: '))
print('Você deve pagar {:.2f}R$ por {}dias e {}km rodados.'.format(((caminho * 0.15)+(dias * 60)), dias, caminho))
