# Criando um dicionário dentro de uma lista

brasil = []    # Lista
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}   # Dicionário
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}        # Dicionário
brasil.append(estado1)
brasil.append(estado2)
print(estado1)    # Mostra o dicionário
print()
print(brasil)     # Mostra a lista, contendo os dicionários
print()
print(brasil[0])  # Mostra o primeiro registro da lista
print()
print(brasil[0]['uf'])  # Mostra o registro uf da lista no campo 0

