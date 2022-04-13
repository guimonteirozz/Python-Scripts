# CONDIÇÕES ANINHADAS #

# ==============================Ex036============================== #
from datetime import date

print('{:=^40}'.format("Ex036"))

valorDaCasa = float(input('Qual o valor da casa: '))
salarioDoComprador = float(input('Qual seu salario: '))
quantidadeDeAnosPagar = float(input('Em quantos anos deseja pagar o emprestimo: '))
prestacaoMensal = (valorDaCasa / quantidadeDeAnosPagar) / 12

if prestacaoMensal <= 0.3*salarioDoComprador:
    print('Emprestimo aceito\nVoce pagara por mes {:.2f} R$'.format(prestacaoMensal))
elif prestacaoMensal > 0.3*salarioDoComprador:
    print('Emprestimo RECUSADO')


# ==============================Ex037============================== #
print('{:=^40}'.format("Ex037"))

numeroInt = int(input('Digite um número inteiro: '))
print('''Escolha uma da opações de conversao: 
1-para-Binário
2-para-Octadecimal
3-para-Hexadecimal''')
escolher = int(input('Digite aqui sua escolha: '))

if escolher == 1:
    print("{} em Binario é = {}".format(numeroInt,bin(numeroInt)[2:]))
elif escolher == 2:
    print("{} em Octadecimal é = {}".format(numeroInt,oct(numeroInt)[2:]))
elif escolher == 3:
    print("{} em Hexadecimal é = {}".format(numeroInt,hex(numeroInt)[2:]))
else:
    print("opção invalida, tente novamente")

# ==============================Ex038============================== #
print('{:=^40}'.format("Ex038"))

valor1 = int(input("Digite 1º valor: "))
valor2 = int(input("Digite 2º valor: "))

if valor1 > valor2:
    print("Primeiro valor é o maior")
elif valor2 > valor1:
    print("Segundo valor é o maior")
else:
    print("Não existe valor maior os dois são iguais")

# ==============================Ex040============================== #
print('{:=^40}'.format("Ex040"))

notaProva1 = float(input("Digite Nota da prova 1: "))
notaProva2 = float(input("Digite Nota da prova 2: "))

mediaProvas = (notaProva1 + notaProva2) / 2

if mediaProvas >= 7.0:
    print("APROVADO com media {:.1f}".format(mediaProvas))
elif mediaProvas <= 6.9 and mediaProvas >= 5.0:
    print("RECUPERAÇÃO com media {:.1f}".format(mediaProvas))
elif mediaProvas < 5.0:
    print("REPROVADO com media {:.1f}".format(mediaProvas))

# ==============================Ex041============================== #
print('{:=^40}'.format("Ex041"))

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
