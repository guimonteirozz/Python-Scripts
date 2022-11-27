from random import choice
from time import sleep

lista = [0,1,2,3,4,5,6,7,8,9,10]
num = choice(lista)

print('\033[1;33m=-=\033[m' * 15)
print('Vou pensar em um número de 0 á 10')
print('\033[1;33m=-=\033[m' * 15)

numb = int(input('Qual número pensei ? '))
print('\033[1;34mPROCESSANDO...\033[m')

sleep(1.5)

if numb == num:
    print('\033[1m-Parabéns-\033[m o número sorteado foi {}, você \033[1;32mVENCEU\033[m'.format(num))
else:
    print('Você \033[1;31mPERDEU\033[m')
    while numb != num:
        print("\033[1;34m=============TENTE NOVAMENTE=============\033[m")
        numb = int(input("\033[1;32mTente Novamente: \033[m"))

        if numb == num:
            print('Voce \033[1;32mVENCEU\033[m \033[1m-Parabéns-\033[m o número sorteado foi {}'.format(num))
        else:
            print('Você \033[1;31mPERDEU DeNOVO\033[m')    
        

