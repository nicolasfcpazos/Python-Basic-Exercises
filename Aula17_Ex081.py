# Crie um programa que leia vários números e coloque em uma lista.
# Depois disso, mostre:

# a) Quantos números foram digitados.
# b) A lista de valores, ordenada de forma decrescente.
# c) Se o valor 5 foi digitado e está ou não na lista.


numeros = []

while True:
    numeros.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar ? [S ou N] ')).strip().upper()[0]
    if resp in 'Nn':
        break
print(f'Você digitou {len(numeros)} números')
numeros.sort(reverse=True)
print(f'A lista em ordem decrescente é: {numeros}')
if 5 in numeros:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não foi encontrado na lista.')


