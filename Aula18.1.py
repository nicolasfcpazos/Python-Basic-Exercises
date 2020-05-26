# AULA DE LISTAS  - PARTE 2  -  LISTA DENTRO DE LISTA

dados = list()
dados.append('Pedro')
dados.append(25)
dados.append('Maria')
dados.append(35)
print(dados)
print('-=' * 15)

# lista dentro de lista

pessoas = list()
pessoas.append(dados[:])   # --> Copia uma lista para dentro de outra
print(pessoas)

print('-=' * 15)

# Outra maneira de criar lista dentro de outra lista

pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas)
print(pessoas[0])     # Imprime o primeiro indice da lista
print(pessoas[0][0])  # resposta: Pedro - Imprime o primeiro indice do primeiro indice
print(pessoas[1][1])  # resposta: 19
print(pessoas[2][0])  # resposta: João