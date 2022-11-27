print('{:=^32}'.format("Data 1")) #07/03/1999
dia1 = int(input("Dia: "))        #10/09/1999  
mes1 = int(input("Mes: "))
ano1 = int(input("Ano: "))

print('{:=^32}'.format("Data 2"))
dia2 = int(input("Dia: "))
mes2 = int(input("Mes: "))
ano2 = int(input("Ano: "))

listMeses = [31,28,31,30,31,30,31,31,30,31,30,31]

somaDias = 0
          
if ano1 == ano2:
    faltaDias1 = listMeses[mes1-1] - dia1

    for i in range(mes1,mes2-1):
        somaDias = somaDias + listMeses[i]
    faltaDias2 = dia2

    totalDias = faltaDias1 + faltaDias2 + somaDias

    if ano1 % 4 == 0 and ano1 % 100 != 0 or ano1 % 400 == 0:
        bixest = totalDias + 1
        print(bixest)
    else:
        print(totalDias)
else:    
    somaDiasD1 = 0
    for i in range(0,mes1-1):
        somaDiasD1 = somaDiasD1 + listMeses[i]

    x = somaDiasD1 + dia1
    diasData1 = 365 - x

    diasAnos = (ano2 - 1) - ano1 
    somaAnos = diasAnos * 365 

    somaDiasD2 = 0
    for p in range(0,mes2-1):
        somaDiasD2 = somaDiasD2 + listMeses[p]

    diasData2 = somaDiasD2 + dia2

    totalDias = diasData1 + diasData2 + somaAnos

    if ano1 % 4 == 0 and ano1 % 100 != 0 or ano1 % 400 == 0:
        bixest = totalDias + (((ano2 - ano1) // 4) + 1)
    elif ano2 % 4 == 0 and ano2 % 100 != 0 or ano2 % 400 == 0:
        bixest = totalDias + (((ano2 - ano1) // 4) + 1)
    else:
        bixest = totalDias + ((ano2 - ano1) // 4)     
 
    print(bixest)