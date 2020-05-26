estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())   # Para copiar o conteudo para o dicionário
print(brasil)
print()

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')

print()

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
