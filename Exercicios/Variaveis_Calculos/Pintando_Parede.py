# Pintando Parede
largura = float(input('Digite a Largura da parede: '))
altura = float(input('Digite a Altura da parede: '))

print('Área da parede é = {:.2f}m²'.format(largura * altura ))
print('Você precisa de {:.2f} litros de tinta para esta parede'.format((largura * altura)/2))