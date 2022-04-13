# ==============================Ex044============================== #
print('{:=^40}'.format("Ex044"))

valorProduto = float(input('Qual o valor do Produto: '))

print('''======-Qual a forma de pagamento-======
1 - Á vista no DINHEIRO/CHEQUE (Descondo de 10%)
2 - Á vista no CARTÃO (Descondo de 5%)
3 - Até 2x no cartão (sem descontos ou juros) 
4 - Até 3x ou mais no cartão (20% de juros) 
''')

formaDePagamento = int(input('Digite aqui a de forma de pagamento: '))

if formaDePagamento == 1 or 2 or 3 or 4:
    if formaDePagamento == 1:
        valorFinal =  valorProduto - (valorProduto * 0.1)
    if formaDePagamento == 2:
        valorFinal = valorProduto - (valorProduto * 0.05)
    if formaDePagamento == 3:
        valorFinal = valorProduto 
    if formaDePagamento == 4: 
        parcelas = int(input("Quantas parcelas: "))

        quantParcelas = valorProduto / parcelas   

        print("Sua compra sera parcelado em {}x de {} com JUROS".format(parcelas, quantParcelas))

        valorFinal = valorProduto + (valorProduto * 0.2)

        print("Sua compra de R${} vai custar R${} no final.".format(valorProduto, valorFinal))

    print('Valor final do seu produto é {:.2f} R$'.format(valorFinal))
else:
    print("VALOR EM INVALIDO, TENTE NOVAMENTE SÓ 1, 2 ou 3")
