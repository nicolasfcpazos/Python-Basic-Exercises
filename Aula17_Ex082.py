# Crie um programa para ler vários números e colocar em uma lista.

# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os
# valores impares digitados, respectivamente.

# Ao final, mostre o conteúdo das três listas geradas.

num = []
par = []
impar = []

while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar ? [S ou N] ')).strip().upper()[0]
    if resp in 'Nn':
        break
for i, v in enumerate(a):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'A lista completa é: {num}')
print('-=' * 15)
print(f'A lista de números pares é: {par}')
print('-=' * 15)
print(f'A lista de números ímpares é: {impar}')
