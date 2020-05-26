# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO QUALQUER E MOSTRE SEU FATORIAL.

# EX: 5! = 5 X 4 X 3 X 2 X 1 = 120

n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end= '')
    f = f * c
    c -= 1
print('{}'.format(f))

# MANEIRA 2 - RESUMIDO

'''from math import factorial
num = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(num)
print('O fatorial de {} é {}'.format(num, f))'''