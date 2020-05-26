# Aprimore o desafio 93 (Jogador futebol), para que ele funcione com
# vários jogadores, incluindo um sistema de visualização de detalhes
# de aproveitamento de cada jogador.

jogador = dict()
time = list()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou ? '))
    partidas.clear()
    for p in range(0, tot):
        partidas.append(int(input(f' Quantos gols na partida {p+1} ? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar cadastrando ? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO ! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-' * 30)
print('cod ', end='')               # Cabeçalho
for i in jogador.keys():
    print(f'{i:<15}', end='')       # Fim do cabeçalho
print()
print('-' * 40)
for k, v in enumerate(time):              # listagem dos dados (tabela)
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')    # fim da listagem dos dados
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador ? [999 para parar] '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro. Não existe jogador com código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('VOLTE SEMPRE !!')
