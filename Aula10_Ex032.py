# FAÇA UM PROGRAMA QUE LEIA UM ANO QUALQUER E MOSTRE SE ELE É BISSEXTO.

import time
from datetime import date

ano = int(input('Que ano você quer analisar ? Coloque 0 para o ano atual: '))

print('-=-' * 15)
print('Vamos verificar se esse ano é Bissexto.')
print('Aguarde estamos calculando...')
time.sleep(1)
print('-=-' * 15)
if ano == 0:
    ano = date.today().year    #mostra o ano atual
if (ano % 4) == 0 and ano %100 != 0 or ano % 400 == 0:
    print('O ano {} é Bissexto.'.format(ano))
else:
    print('O ano {} não é Bissexto'.format(ano))

