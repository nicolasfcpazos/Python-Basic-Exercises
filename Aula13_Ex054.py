# CRIE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE SETE PESSOAS.
# NO FINAL, MOSTRE QUANTAS PESSOAS AINDA NÃO ATINGIRAM A MAIORIDADE E QUANTAS
# JÁ SÃO MAIORES.

from datetime import date

atual = date.today().year
menor = 0
maior = 0

for c in range(1, 8):
    nasc = int(input('Em que ano a {}a pessoa nasceu? '.format(c)))
    idade = atual - nasc
    if idade <= 21:
        menor += 1
    else:
        maior += 1
print('-='*20)
print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('E também tivemos {} pessoas menores de idade'.format(menor))
