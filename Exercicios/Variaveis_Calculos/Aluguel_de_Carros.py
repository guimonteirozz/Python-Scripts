# Aluguel de Carros 60 reais por dia 0,15 por km rodado

caminho = float(input('Quantos km você percorreu por com o carro: '))
dias = int(input('Quantos dias você ficou com o carro: '))

print('Você deve pagar {:.2f}R$ por {}dias e {}km rodados.'.format(((caminho * 0.15)+(dias * 60)), dias, caminho))