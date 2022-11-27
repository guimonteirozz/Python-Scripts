valor = int(input("Qual numero deseja saber a tabuada: "))
tamanho = int(input("Até onde vai sua tabuada: "))

for tamanho in range(1, tamanho + 1):
    produto = tamanho * valor

    print(f"{tamanho} x {valor} = {produto}")
