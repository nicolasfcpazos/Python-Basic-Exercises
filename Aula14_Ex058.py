# MELHORE O JOGO DO DESAFIO 028 ONDE O COMPUTADOR VAI "PENSAR" EM UM
# NÚMERO ENTRE 0 E 10. # SÓ QUE AGORA O JOGADOR VAI TENTAR ADIVINHAR
# ATÉ ACERTAR, MOSTRANDO NO FINAL QUANTOS # PALPITES FORAM NECESSÁRIOS
# PARA VENCER.

from random import randint
from time import sleep

computador = randint(0, 10)
acertou = False
tentativas = 0
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)

while not acertou:
    jogador = int(input('Em que número eu pensei ? '))
    tentativas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Parabéns. Você acertou com {} tentativas.'.format(tentativas))