print('{:=^40}'.format('Exx034'))

salario = float(input('Digite seu salário: '))
if salario <= 1.250:
    print('Seu salário é {:.2f} R$ com aumento de 15%'.format((salario * 0.15) + salario))
else:
    print('Seu salário é {:.2f} R$ com aumento de 10%'.format((salario * 0.10) + salario))

'''
Ex034 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
'''