notaProva1 = float(input("Digite Nota da prova 1: "))
notaProva2 = float(input("Digite Nota da prova 2: "))

mediaProvas = (notaProva1 + notaProva2) / 2

if mediaProvas >= 7.0:
    print("APROVADO com media {:.1f}".format(mediaProvas))
elif mediaProvas <= 6.9 and mediaProvas >= 5.0:
    print("RECUPERAÇÃO com media {:.1f}".format(mediaProvas))
elif mediaProvas < 5.0:
    print("REPROVADO com media {:.1f}".format(mediaProvas))
