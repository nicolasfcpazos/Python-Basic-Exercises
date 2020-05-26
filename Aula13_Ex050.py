# DESENVOLVA UM PROGRAMA QUE LEIA SEIS NÚMEROS INTEIROS E MOSTRE A SOMA APENAS
# DAQUELES QUE FOREM PARES. SE O VALOR DIGITADO FOR ÍMPAR, DESCONSIDERE-O.


print('VAMOS SOMAR OS NÚMEROS QUE FOREM DIGITADOS E FOREM PARES')
print('-='*28)
quant = int(input('Quantos números você quer ler ? '))
soma = 0
cont = 0
for c in range(1, quant+1):
    n = int(input('Digite o {}o número: '.format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('-='*17)
print('Somando apenas os números pares...')
print('-='*17)
print('Você informou {} números pares e a soma dos números é {}'.format(cont, soma))


