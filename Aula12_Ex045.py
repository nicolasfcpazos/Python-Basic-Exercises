# CRIE UM PROGRAMA QUE FAÇA O COMPUTADOR JOGAR JOQUENPÔ COM VOCÊ.

from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('-='*15)
print('VAMOS JOGAR JOKENPÔ ?')
print('='*15)
print('''Suas opções: 
[0] Pedra
[1] Papel 
[2] Tesoura''')
print('-='*15)
jogador = int(input('Qual é a sua jogada ? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ !!!')
sleep(1)
print('-='*15)
print('O Computador jogou {}'.format(itens[computador]))
print('O Jogador jogou {}'.format(itens[jogador]))
print('-='*15)
if computador == 0:      # COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print('EMPATE !')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA ! TENTE NOVAMENTE !')
elif computador == 1:    # COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE !')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA ! TENTE NOVAMENTE !')
elif computador == 2:    # COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE !')
    else:
        print('JOGADA INVÁLIDA ! TENTE NOVAMENTE !')
