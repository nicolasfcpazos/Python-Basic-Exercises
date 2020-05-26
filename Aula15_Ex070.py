# Faça um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:

# a) qual o total gasto na compra.
# b) quantos produtos custam mais de R$ 1000.
# c) qual é o nome do produto mais barato.

total = 0
totmil = 0
menor = 0
cont = 0
barato = ''
print('*' * 25)
print('   LOJAS BRASILEIRAS')
while True:
    print('*' * 25)
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco
    if preco >= 1000:
        totmil += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar ? [S ou N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' COMPRA FINALIZADA '))
print('*' * 25)
print(f'O total da compra foi R$ {total:.2f}')
print(f'{totmil} produtos custam mais de R$ 1.000,00')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')
