# Aprimore o desafio 86, mostrando no final:

# a) A soma de todos os valores pares digitados.
# b) A soma dos valores da terceira coluna.
# c) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = 0
soma3 = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
    soma3 += matriz[l][2]
print('-=' * 20)
print(f'Matriz 3 x 3: {matriz}')
for l in range(0, 3):
    print(f'  A linha {l + 1}: ', end='')
    for c in range(0, 3):
        print(f' [{matriz[l][c]:^4}] ', end='')
    print()
print('-=' * 20)
print(f'A soma dos valores pares é: {somapar}')
print(f'A soma da terceira coluna é: {soma3}')
print(f'O maior valor da linha 2 é: {max(matriz[1])}')

