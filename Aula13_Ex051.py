# DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE UMA PA (PROGRESSÃO
# ARITMÉTICA). NO FINAL, MOSTRE OS 10 PRIMEIROS TERMOS DESSA PROGRESSÃO.

from time import sleep

print('10 PRIMEIROS TERMOS DE UMA PROGRESSÃO ARITMÉTICA !')
print('-='*30)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
print('-='*30)
print('Calculando...')
sleep(1)
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{} '.format(c), end= '-> ')
print('FIM')
