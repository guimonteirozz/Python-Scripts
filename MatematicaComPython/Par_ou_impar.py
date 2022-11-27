print('{:=^40}'.format('Exx030'))

numero = int(input('Digite um número: '))

par = numero // 2

if numero/2 == par:
    print(f'{numero} é PAR')
else:
    print(f'{numero} é ÍMPAR')