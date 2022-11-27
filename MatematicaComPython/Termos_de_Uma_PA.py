# Progessao Aritimética
print('''
==========================
   10 TERMOS DE UMA PA
==========================
''')
pTermo = int(input('Qual o primeiro termo da sua PA: '))
razao = int(input('Qual a razão da sua PA: '))
decimoTermo = pTermo + 9 * razao

for k in range (pTermo, decimoTermo + razao,razao):
    print(k, end=' -> ')
print('ACABOU')
