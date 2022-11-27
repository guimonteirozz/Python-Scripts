# Ex025-Procurando uma string dentro da outra REVER #
print('{:=^40}'.format('Ex025'))

nomeInserido = str(input("Qual seu nome completo: ")).strip()
sobrenomeSilva = 'silva' in nomeInserido.lower()

if sobrenomeSilva == True:
    print('Tem Silva no Seu Nome')
else:
    print('Nâo Tem Silva no Seu Nome')