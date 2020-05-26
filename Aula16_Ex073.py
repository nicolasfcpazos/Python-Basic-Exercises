# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato
# Brasileiro de Futebol, na ordem de colocação. Depois mostre:

# a) Apenas os 5 primeiros colocados.
# b) Os últimos 4 colocados na tabela.
# c) Uma lista com os times em ordem alfabética.    --> comando sorted
# d) Em que posição na tabela está o time da Chapecoense.

times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR',
         'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás',
         'Bahia', 'Vasco da Gama', 'Atlético-MG', 'Fluminense', 'Botafogo',
         'Ceará', 'Cruzeiro', 'Csa', 'Chapecoense', 'Avaí')

print(' CAMPEONATO BRASILEIRO 2019')
print(f'Os 5 primeiros colocados foram: {times[0:5]}')
print('-=' * 20)
print(f'Os 4 últimos colocados (rebaixados) foram: {times[-4:]}')
print('-=' * 20)
print(f'Os times em ordem alfabética são: {(sorted(times))}')
print('-=' * 20)
print(f'O time da Chapecoense ficou na: {times.index("Chapecoense")+1}a posição')


