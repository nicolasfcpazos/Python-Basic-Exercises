# Dicionários
pessoas = {'nome': 'Nicolas', 'sexo': 'M', 'idade': 40}
print(pessoas)
print()
print(pessoas['nome'])
print()
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print()
print(pessoas.keys())
print()
print(pessoas.values())
print()
print(pessoas.items())
print()

# del pessoas['sexo']   # para deletar um registro

pessoas['nome'] = 'Leandro'   # Utilizado para trocar o conteúdo
pessoas['peso'] = 98.5   # insere um item novo no dicionário

for k in pessoas.values():  # Mostra o conteudo dos indices
    print(k)
print()
for k in pessoas.keys():    # Mostra o nome(chaves) dos indices
    print(k)
print()
for k, v in pessoas.items(): # MOstra a chave e o conteúdo
    print(f'{k} = {v}')
