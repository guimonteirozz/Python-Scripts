from datetime import date

genero = str(input("Digite seu genero (F/H): ")).upper()

if genero == 'F':
    print("Você não precisa fazer alistamnto obrigatorio")
else:
    anoNascimento = int(input("Digite o ano de seu nascimento: "))

    anoAtual = date.today().year
    idade = anoAtual - anoNascimento
    anoAlistamento = anoNascimento + 18
    tempoParaAlistamento = anoAtual - anoNascimento
    atrasoParaAlistamento = anoAtual - anoAlistamento

    if idade < 18:
        print("Quem nasceu em {} tem {} anos em {}".format(anoNascimento, idade, anoAtual))
        print("Ainda faltam {} anos para o alistamento e".format(tempoParaAlistamento))
        print("Seu alisteamento será em {}".format(anoAlistamento))
    
    elif idade == 18:
        print("Quem nasceu em {} tem {} anos em {}".format(anoNascimento, idade, anoAtual))
        print("ja pode se alistar esse ano {} IMENTIATAMENTE".format(anoAtual))
    
    elif idade > 18:
        print("Quem nasceu em {} tem {} anos em {}".format(anoNascimento, idade, anoAtual))
        print("ja Deveria ter se alistado há {} atras em {}".format(atrasoParaAlistamento, anoAlistamento))
    