# CRIE UM PROGRAMA QUE CALCULE A SOMA ENTRE TODOS OS NÚMEROS ÍMPARES QUE SÃO
# MÚLTIPLOS DE TRÊS E QUE SE ENCONTREM NO INTERVALO DE 1 ATÉ 500.

cont = 0
s = 0
for c in range(1, 501, 2):
    if c % 3 == 0 and c % 2 != 0:
        print(c)
        s += c
        cont = cont + 1
print('O somatório de todos os {} números múltiplos de 3 é {}'.format(cont, s))
print('FIM')


