# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador PERDER, mostrando o total
# de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

v = 0
print('-=-' * 20)
print('Vamos jogar PAR ou ÍMPAR ?')
print('-=-' * 20)

while True:
    jogador = int(input('Escolha um numero: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou ímpar ? [P ou I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}. ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    print('-=-' * 10)
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU !')
            v += 1
        else:
            print('VOCÊ PERDEU !')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Vocẽ venceu !')
            v += 1
        else:
            print('VOCÊ PERDEU !')
            break
    print('Vamos jogar novamente...')
    print('-=-' * 10)
print(f'GAME OVER ! Você venceu {v} vezes.')


