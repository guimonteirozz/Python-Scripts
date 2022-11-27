# ==============================Ex045============================== #
from random import choice
from time import sleep

print ('{:=^40}'.format ("Ex045"))

print ("====O que vai jogar====")
jogador = input ("Pedra - Tesoura - Papel: ").title() 

if jogador == 'Pedra' or jogador == 'Tesoura' or jogador == 'Papel':
    print ("Você jogou {}".format(jogador))
    print ("e...")
    sleep (1.5)

    lista = ['Pedra', 'Papel', 'Tesoura']
    maquina = choice(lista)

    print ("A maquina jogou {}".format(maquina))
    
    if maquina == jogador:
        partida = "Partida Empatada"

    elif maquina == 'Pedra' and jogador == 'Papel':
        partida = "Você ganhou"
    elif maquina == 'Papel' and jogador == 'Pedra':
        partida = "Você perdeu e a maquina ganhou"

    elif maquina == 'Papel' and jogador == 'Tesoura':
        partida = "Você ganhou"
    elif maquina == 'Tesoura' and jogador == 'Papel':
        partida = "Você perdeu e a maquina ganhou"

    elif maquina == 'Tesoura' and jogador == 'Pedra':
        partida = "Você ganhou"
    elif maquina == 'Pedra' and jogador == 'Tesoura':
        partida = "Você perdeu e a maquina ganhou"
else:
    partida = "Valor invalido, tente novamente"

print(partida)
