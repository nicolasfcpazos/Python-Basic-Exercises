# Leia a largura e a altura de uma parede
# Calcule sua área e a quantidade de tinta necessária para pintá-la
# sabendo que cada uma lata de tinta pinta uma área de 2m2.

altura = float(input ('Qual a altura da parede: '))
largura = float(input ('Qual a largura da parede: '))
espaco = altura * largura
tinta = espaco / 2
print('Sua parede tem a dimensão de {:.2f} x {:.2f} e sua área é de {:.2f} m2.'.format(altura, largura, espaco))
print('Para pintar essa parede, você precisará de {:.2f} litros de tinta.'.format(tinta))



