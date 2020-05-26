# Exemplos

valores = []   # --> Criar uma lista vazia     ou   valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)
print('-=' * 10)

for v in valores:
    print(f'{v}...', end='')
print('\n')
print('-=' * 10)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v} !')
print('Cheguei ao final da lista')
print('-=' * 10)

# Exemplo 3

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(valores)

