# FAÇA UM PROGRAMA QUE LEIA UM ÂNGULO QUALQUER E MOSTRE NA TELA O VALOR DO SENO, COSSENO E
# TANGENTE DESSE ANGULO.

from math import radians, sin, cos, tan

print('Vamos calcular o Seno, Cosseno e a Tangente de um ângulo !)')
angulo = float(input('Digite um ângulo a ser calculado: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('O seno do ângulo é {:.2f}'.format(seno))
print('O cosseno do ângulo é {:.2f}'.format(cosseno))
print('A tangente do ângulo é {:.2f}'.format(tangente))
