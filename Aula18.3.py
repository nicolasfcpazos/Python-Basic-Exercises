# continua Lista - parte 2


galera = list()
dado = list()
totmai = totmen = 0

# ler os dados
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
# compara para ver quem é menor e maior de idade
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
# mostra o resultado
print(f'Temos {totmai} maiores e {totmen} menores de idade')

