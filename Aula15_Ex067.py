# Faça um programa que leia a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário. O programa será interrompido
# quando o número solicitado for negativo.


print('------- TABUADA -------')
cont = 0

while True:
    num = int(input('Digite um número para ver sua tabuada: '))
    print('-' * 30)
    if num < 0:
        break
    for cont in range(1, 11):
        print(f'{num} x {cont} = {(num * cont)}')
    print('-' * 30)
print('Programa encerrado. Volte sempre !!')
