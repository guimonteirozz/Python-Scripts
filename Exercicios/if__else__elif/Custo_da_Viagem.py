print('{:=^40}'.format('Exx031'))

viagem = int(input('Digite a distancia de sua viagem: '))

if viagem <= 200:
    print('Sua passagem custa {:.2f} R$'.format(viagem * 0.50))
else:
    print('Sua passagem custa {:.2f} R$'.format(viagem * 0.45))

'''
Ex031 - Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
'''