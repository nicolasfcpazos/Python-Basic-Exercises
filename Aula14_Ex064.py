# CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS. O PROGRAMA SÓ VAI PARA QUANDO O
# OSUÁRIO DIGITAR O VALOR 999, QUE É A CONDIÇÃO DE PARADA. NO FINAL,
# MOSTRE QUANTOS NÚMEROS FORAM DIGITADOS E QUAL FOI A SOMA ENTRE
# ELES (DESCONSIDERANDO O FLAG - 999)

print('-'*30)
n = 0
soma = 0
cont = 0
n = int(input('Digite um número: [999 para parar]: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número: [999 para parar]: '))
print('Vocẽ digitou {} números e a soma entre eles foi {}'.format(cont, soma))



