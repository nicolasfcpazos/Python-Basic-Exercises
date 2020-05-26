# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feito em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o
# total de gols feitos durante o campeonato.

jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou ? '))
for p in range(0, tot):
    partidas.append(int(input(f' Quantos gols na partida {p+1} ? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)

for k, v in jogador.items():               # Mostra a chave e o conteúdo
    print(f'O campo {k} tem o valor {v}')

print('-=' * 30)
print(f'O jogador {jogador["nome"]} tem {len(jogador["gols"])} partidas.')
print('-=' * 30)

for k, v in enumerate(jogador['gols']):               # Mostra a chave e o conteúdo
    print(f'=> Na partida {k+1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')