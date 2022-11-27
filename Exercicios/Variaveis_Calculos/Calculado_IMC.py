# ==============================Ex043============================== #
print('{:=^40}'.format("Ex043"))

peso = float(input('Digite seu peso: '))
altura = float(input('Difgite sua altura: '))

imc = peso / (altura * altura)

if imc < 18.5:
    categoria = 'Abaixo do Peso'
elif imc >= 18.5 and imc < 25:
    categoria = 'Peso Ideal'
elif imc >= 25 and imc < 30:
    categoria = 'Sobrepeso'
elif imc >= 30 and imc < 40:
    categoria = 'Obesidade'
elif imc > 40:
    categoria = 'Obesidade Mórbida'

print('Seu Indice de Massa Corporal deu {:.2f}'.format(imc))
print('Sua Categoria é {}'.format(categoria))

# imc peso / altura elevado au quadrado