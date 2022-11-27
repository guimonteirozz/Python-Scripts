valorDaCasa = float(input('Qual o valor da casa: '))

salarioDoComprador = float(input('Qual seu salario: '))

quantidadeDeAnosPagar = float(input('Em quantos anos deseja pagar o emprestimo: '))

prestacaoMensal = (valorDaCasa / quantidadeDeAnosPagar) / 12

if prestacaoMensal <= 0.3 * salarioDoComprador:
    print('Emprestimo aceito\nVoce pagara por mes {:.2f} R$'.format(prestacaoMensal))
elif prestacaoMensal > 0.3 * salarioDoComprador:
    print('Emprestimo RECUSADO')
