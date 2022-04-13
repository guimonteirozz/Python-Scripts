numb = int(input("Digite um número: "))

if numb <= 1:
    print("**O NÚMERO DIGITADO TEM QUE SER MAIOR QUE 1**")
else:
    for i in range(2,numb):
        if numb % i == 0:  
            numbPrimo = 'Não é primo'
            break
        else:
            numbPrimo = 'É primo'
    print("O Número {} {}".format(numb,numbPrimo))
