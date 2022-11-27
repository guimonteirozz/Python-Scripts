from datetime import date

ano = int(input('Digite um ano ou digite 0 para saber o ano atual : '))
if ano == 0:
    ano = date.today().year # ano de hoje 24/01/22 #
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')

# o sistema fala se o ano de netrada e bissexto ou nao