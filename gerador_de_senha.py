from random import choices

lette_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lette_lower = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'
symbols = '@#$%&*_+=!,.'

total = lette_upper + lette_lower + numbers + symbols

numero_caracteres = int(input('Numero de Caracteres da senha: '))

while numero_caracteres < 8:
    print('O NUMERO DE CARACTERES TEM QUE SER MAIOR OU IGUAL A 8')
    numero_caracteres = int(input('Numero de Caracteres da senha: '))

list_str = ','.join(choices(total, k=numero_caracteres))
print(list_str.replace(',', ''))
