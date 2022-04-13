from datetime import date
soma = 0
anoAtual = date.today().year

for i in range(0,7):
    nascimento = int(input("Digite o ano de nascimento da pessoa {}: ".format(i+1)))

    idade = anoAtual - nascimento

    if idade >= 21:
        soma += 1 

print("Das 7 pessoas, {} são maior de idade".format(soma))
print("É {} são menores de idade".format(7-soma))

