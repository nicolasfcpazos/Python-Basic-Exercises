# LEIA UM NÚMERO REAL QUALQUER PELO TECLADO E MOSTRE NA TELA  A SUA PORÇÃO REAL.

from math import trunc

n = float(input('Insira um número real: '))

print('O número {} e sua porção inteira é {}'.format(n, trunc(n))) # Usando função
print('O número {} e sua porção inteira é {}'.format(n, int(n)))  # retorno número inteiro sem função



