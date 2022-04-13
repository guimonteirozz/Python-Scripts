# Ex028-Jogo de adivinhação V1.0 #
from random import choice
from time import sleep

# escolher o numero do computador #
print('{:=^40}'.format('Exx028'))
lista = [0, 1, 2, 3, 4, 5]
num = choice(lista)
print('\033[1;33m=-=\033[m' * 15)
print('Vou pensar em um número de 0 á 5')
print('\033[1;33m=-=\033[m' * 15)
numb = int(input('Qual número pensei ? '))
print('\033[1;34mPROCESSANDO...\033[m')
sleep(1.5)
if numb == num:
    print('\033[1m-Parabéns-\033[m o número sorteado foi {}, você \033[1;32mVENCEU\033[m'.format(num))
else:
    print('Você \033[1;31mPERDEU\033[m, o número sorteado foi {} e não {}'.format(num, numb))

# Ex029-Radar eletrônico #
print('{:=^40}'.format('Exx029'))
velocidade = int(input('Digite a Velocidade do seu carro: '))
multa = float((velocidade - 80) * 7)
if velocidade > 80:
    print('Você foi multado no valor de {:.2f} R$'.format(multa))
else:
    print('Sua Velocidade foi {} Km/h e Você não foi multado'.format(velocidade))

# Ex030-Par ou ímpar REVER#
print('{:=^40}'.format('Exx030'))
numero = int(input('Digite um número: '))
par = numero // 2
if numero/2 == par:
    print('{} é PAR'.format(numero))
else:
    print('{} é ÍMPAR'.format(numero))

# Ex031-Custa de uma viagem #
print('{:=^40}'.format('Exx031'))
viagem = int(input('Digite a distancia de sua viagem: '))
if viagem <= 200:
    print('Sua passagem custa {:.2f} R$'.format(viagem * 0.50))
else:
    print('Sua passagem custa {:.2f} R$'.format(viagem * 0.45))

# Ex032-Ano bixesto REVER e CONSERTAR#
print('{:=^40}'.format('Exx032'))
from datetime import date
ano = int(input('Digite um ano ou digite 0 para saber o ano atual : '))
if ano == 0:
    ano = date.today().year # ano de hoje 24/01/22 #
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))

# Ex033-Maior e menor valores REVER#
print('{:=^40}'.format('Exx033'))
numb1 = int(input('Digite o 1º número: '))
numb2 = int(input('Digite o 2º número: '))
numb3 = int(input('Digite o 3º número: '))
if numb1 < numb2 and numb1 < numb3:
    menor = numb1
if numb2 < numb1 and numb2 < numb3:
    menor = numb2
if numb3 < numb1 and numb3 < numb2:
    menor = numb3
if numb1 < numb2 and numb1 < numb3:
    maior = numb1
if numb2 > numb1 and numb2 > numb3:
    maior = numb2
if numb3 > numb1 and numb3 > numb2:
    maior = numb3
print('Maior número é {}'.format(maior))
print('Menor número é {}'.format(menor))

# Ex034-Aumentando mútiplos#
print('{:=^40}'.format('Exx034'))
salario = float(input('Digite seu salário: '))
if salario <= 1.250:
    print('Seu salário é {:.2f} R$ com aumento de 15%'.format((salario * 0.15) + salario))
else:
    print('Seu salário é {:.2f} R$ com aumento de 10%'.format((salario * 0.10) + salario))

# Ex035-Analisando Triangulo v1.0#
print('{:=^40}'.format('Exx035'))
reta1 = float(input('Reta 1: '))
reta2 = float(input('Reta 2: '))
reta3 = float(input('Reta 3: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Pode ser um triangulo')
else:
    print('Não pode ser um triangulo')
