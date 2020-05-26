# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final mostre:

# a) Quantas vezes aparece o número 9.
# b) Em que posição foi digitado o primeiro valor 3.
# c) Quais foram os pares.

num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
par = 0
print('-' * 20)
print(f'Você digitou os números {num}')
print(f'O número 9 aparece {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}a posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
#print(f'Os números pares são: {par}')
