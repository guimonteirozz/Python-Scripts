frase = input("Digite uma frase: ").upper().replace(' ','').strip()
inverso = ''
tamanhoFrase = len(frase) 

for a in range(0,tamanhoFrase):
    inverso += frase[(tamanhoFrase - 1) - a]
    if frase[a] == frase[(tamanhoFrase - 1) - a]:
        resultado = "É um Políndromo"
        
    else:
        resultado = "Não é um Políndromo"

print('a Frase {} ao contrario é {} então {}'.format(frase,inverso,resultado))        
