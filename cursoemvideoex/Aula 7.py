#Ex005 Antecessor e Sucessor
print('{:=^40}'.format("Ex005-Antecessor e Sucessor"))
n = int(input('Digite um Número Inteiro: '))
print('Antecessor = {}'.format(n - 1))
print('Sucessor = {}'.format(n + 1))

#Ex006 Dobro, Triplo e Raiz Quadrada
print('{:=^40}'.format('Ex006-Dobro, Triplo e Raiz Quadrada'))
n1 = int(input('Digite um Valor Inteiro: '))
print('Dobro de {} é = {}'.format(n1, n1 * 2))
print('Triplo de {} é = {}'.format(n1, n1 * 3))
print('Raiz Quadrada de {} = {}'.format(n1, n1 * n1))

#Ex007 Média Aritmética
print('{:=^40}'.format('Ex007-Média Aritmética'))
nota1 = float(input('Digite a Nota 1: '))
nota2 = float(input('Digite a nota 2: '))
print('Media do aluno = {:.1f}'.format((nota1 + nota2)/2))

#Ex008 Converso de medidas
print("{:=^40}".format('Ex008-Conversor de Medidas'))
metro = int(input('Digite um Valor em Metros: '))
print('Valor em Quilômetro = {}km'.format(metro * 0.001))
print('Valor em Hectômetro = {}hm'.format(metro * 0.01))
print('Valor em Decâmetro = {}dam'.format(metro * 0.1))
print('Valor em Metro = {}m'.format(metro))
print('Valor em Decímentro = {}dm'.format(metro * 10))
print('Valor em Centímetros = {}cm'.format(metro * 100))
print('Valor em Milímetros = {}mm'.format(metro * 1000))

#Ex009 Tabuada
print('{:=^40}'.format('Ex009-Tabuada'))
valor = int(input('Digite um valor: '))
print('{:-^25}'.format("Tabuada do {}".format(valor)))
print('{} x 1 = {}'.format(valor, valor * 1))
print('{} x 2 = {}'.format(valor, valor * 2))
print('{} x 3 = {}'.format(valor, valor * 3))
print('{} x 4 = {}'.format(valor, valor * 4))
print('{} x 5 = {}'.format(valor, valor * 5))
print('{} x 6 = {}'.format(valor, valor * 6))
print('{} x 7 = {}'.format(valor, valor * 7))
print('{} x 8 = {}'.format(valor, valor * 8))
print('{} x 9 = {}'.format(valor, valor * 9))
print('{} x 10 = {}'.format(valor, valor * 10))

#Ex010 Conversor de Moedas
print('{:=^40}'.format('Ex010-Conversor de Moedas'))
moeda = float(input('Digite o valor EM REAL, para saber quantos dalores você pode comprar: '))
print('Você pode comprar {:.2f} dólares'.format(moeda / 3.27))

#Ex011 Pintando Parede
print('{:=^40}'.format('Ex011-Pintando Parede'))
largura = float(input('Digite a Largura da parede: '))
altura = float(input('Digite a Altura da parede: '))
print('Área da parede é = {:.2f}m²'.format(largura * altura ))
print('Você precisa de {:.2f} litros de tinta para esta parede'.format((largura * altura)/2))

#Ex012 Calculando Desconto
print('{:=^40}'.format('Ex012-Calculando Desconto'))
preco = float(input('Digite o preço do produto: '))
print('Preço do produto com 5% de desconto é = {:.2f}R$'.format(preco - (preco * 0.05)))

#Ex013 Reajuste Salrial
print('{:=^40}'.format('Ex013-Reajuste Salarial'))
salario = float(input('Digite seu salario: '))
print('Seu novo sálario com aumento de 15% é = {:.2f}R$'.format(salario + (salario * 0.15)))
