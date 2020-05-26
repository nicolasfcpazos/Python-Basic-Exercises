#  LEIA O COMPRIMENTO DO CATETO OPOSTO E DO CATETO ADJACENTE DE UM TRIÂNGULO
# RETÂNGULO, CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA.

from math import hypot

print('Cálculo da hipotenusa de um Triângulo Retângulo !')
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite p comprimento do cateto adjacente: '))

hi = hypot(co, ca)

print('A hipotenusa vai medir {:.2f}'.format(hi))


