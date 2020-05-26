# CRIE UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA
# SE ELE É PAR OU IMPAR

numero = int(input('Digite um número inteiro: '))
if (numero % 2) == 0:
    print('O Número {} é PAR !'.format(numero))
else:
    print('O número {} é ÍMPAR !'.format(numero))
