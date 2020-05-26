# LIGAÇÃO ENTRE LISTA

a = [2, 3, 4, 7]
b = a       # faz uma ligação com a lista a --> não é uma cópia
b[2] = 8    # altera o 2o registro para o objeto 8 --> irá alterar tb na lista A
print(f'A Lista A: {a}')
print(f'A Lista B: {b}')

print('')

# cópia de uma lista

a = [2, 3, 4, 7]
b = a[:]      # faz uma CÓPIA da lista A
b[2] = 8    # altera o 2o registro para o objeto 8 --> APENAS na lista B
print(f'A Lista A: {a}')
print(f'A Lista B: {b}')