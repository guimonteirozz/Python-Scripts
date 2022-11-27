# Ex029-Radar eletrônico #
print('{:=^40}'.format('Exx029'))

velocidade = int(input('Digite a Velocidade do seu carro: '))

multa = float((velocidade - 80) * 7)
if velocidade > 80:
    print('Você foi multado no valor de {:.2f} R$'.format(multa))
else:
    print('Sua Velocidade foi {} Km/h e Você não foi multado'.format(velocidade))