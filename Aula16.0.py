# TUPLAS  -- TUPLAS SÃO IMUTÁVEIS

lanche = ('Hambuguer', 'Suco', 'Pizza', 'Pudim')

# EXEMPLO 1
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

print('-' * 20)

# EXEMPLO 2
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba !')

print('-' * 20)

# EXEMPLO 3
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

# visualizar elementos dentro da tupla
'''print(lanche)        # MOSTRA TODOS OS ELEMENTOS
print(lanche[1])     # MOSTRA O ELEMENTO NA POSIÇÃO 1
print(lanche[1:3])   # MOSTRA OS ELEMENTOS COMEÇANDO NA POSIÇÃO 1 ATÉ A 2 (A 3 É DESPREZADA)
print(lanche[2:])    # MOSTRA OS ELEMENTOS INICIANDO NA POSIÇÃO ATÉ O FINAL
print(lanche[:2])    # MOSTRA OS ELEMENTOS DESDE O INÍCIO ATÉ A POSIÇÃO 1 (DESPREZANDO A 2)
print(lanche[-1])    # MOSTRA O ÚLTIMO ELEMENTO'''



