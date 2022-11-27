cor = {'azul':'\033[33;1m','vermelho':'\033[31;1m'}
cout = 0
numb = int(input('Digite um Número: '))

if numb <= 1:
    print("**O NÚMERO DIGITADO TEM QUE SER MAIOR QUE 1**")
else:
    for i in range(1,numb+1):
        if numb % i == 0:
            print(cor['azul'],i,cor['azul'],end='')
            cout += 1
        else:
            print(cor['vermelho'],i,cor['vermelho'],end='')
    if cout == 2:
        primo = 'O NÚMERO É PRIMO'
    else:
        primo = 'O NÚMERO NÃO É PRIMO'
    print('\n\033[1;37m O Número {} foi divisivel {} vezes Então {}\033[m'.format(numb,cout,primo))