# Faça um programa que leia o nome e o peso de várias pessoas, guardando tudo
# em uma lista. No final, mostre:

# a) quantas pessoas foram cadastradas
# b) uma listagem com as pessoas mais pesadas. 100 kg
# c) uma listagem com as pessoas mais leves. 70kg

dado = list()
pessoas = list()
maior = 0
menor = 0

while True:
    dado.append(str(input('Nome da pessoa: ')))
    dado.append(float(input('Digite o peso [em KG]: ')))
    if len(pessoas) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    pessoas.append(dado[:])
    dado.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar ? [S ou N] ')).strip().upper()[0]
    if resp in 'N':
        break
print('-=' * 20)
print(f'Ao todo, {len(pessoas)} pessoas foram cadastradas')
print()
print(f'O maior peso foi de {maior} kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor} kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()