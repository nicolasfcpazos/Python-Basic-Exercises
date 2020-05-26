# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário. No final, coloque esse dicionário em
# ordem, sabendo que o vencedor tirou o maior número no dado.

#  Ex:  Valores sorteados:
#           O jogador1 tirou
#           O jogador2 tirou
#           O jogador3 tirou
#           O jogador4 tirou
#       Ranking dos jogadores:
#           1o lugar: jogador1 com
#           2o lugar: jogador1 com
#           3o lugar: jogador1 com
#           4o lugar: jogador1 com

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('-=' * 15)
print('VALORES SORTEADOS:')
for k, v in jogo.items():               # Mostra a chave e o conteúdo
    sleep(1)
    print(f'  O {k} tirou {v} no dado')
print('-=' * 15)
print('RANKING DOS JOGADORES:')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) # Organiza dentro do dicionário
for i, v in enumerate(ranking):
    print(f'  {i+1}o lugar: {v[0]} com {v[1]}.')
    sleep(1)
