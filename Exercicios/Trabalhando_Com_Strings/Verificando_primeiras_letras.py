# Ex024-Verificando as primeiras letras de um texto REVER #

print('{:=^40}'.format('Ex024'))

cidade = str(input('Qual cidade você nasceu ')).strip()

print(cidade[:5].upper() == 'SANTO')