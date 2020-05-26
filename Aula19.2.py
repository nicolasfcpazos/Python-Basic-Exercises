# DICIONÁRIO


# OUTRO EXEMPLO

filme = {'titulo':'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'
}
print(filme)
print()
print(filme.values())   # Retorna todos os valores do dicionário
print()
print(filme.keys())     # Retorna as chaves(indices) do dicionário
print()
print(filme.items())    # Retorna os valores e as chaves do dicionário

print()

for k, v in filme.items():
    print(f'O {k} é {v}')  