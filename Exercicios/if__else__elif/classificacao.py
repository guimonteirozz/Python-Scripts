from datetime import date

anoNascimentoNatacao = int(input('Digite o ano de nascimento: '))

dataHoje = date.today().year

idadeNatacao = dataHoje - anoNascimentoNatacao

if idadeNatacao <= 9:
    categoria = "MIRIM"
elif idadeNatacao <= 14:
    categoria = "INFANTIL"
elif idadeNatacao <= 19:
    categoria = "JUNIOR"
elif idadeNatacao <= 25:
    categoria = "SÊNIOR"
elif idadeNatacao > 25:
    categoria = "MASTER"

print("Com {} anos.".format(idadeNatacao))
print("Sua categoria é {}".format(categoria))
