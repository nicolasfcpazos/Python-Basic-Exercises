# FAÇA UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO. NO FINAL
# DA EXECUÇÃO, MOSTRE A MÉDIA ENTRE TODOS OS VALORES E QUAL FOI O MAIOR
# E O MENOR VALORES LIDOS. O PROGRAMA DEVE PERGUNTAR AO USUÁRIO SE ELE
# QUER OU NÃO CONTINUAR A DIGITAR VALORES.


resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
media = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, media))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))
print('ACABOU')

