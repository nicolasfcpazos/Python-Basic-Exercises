# CRIE UM PROGRAMA QUE LEIA DOIS VALORES E MOSTRE UM MENU NA TELA:

# [1] SOMAR
# [2] MULTIPLICAR
# [3] MAIOR
# [4] NOVOS NÚMEROS
# [5] SAIR DO PROGRAMA

# SEU PROGRAMA DEVERÁ REALIZAR A OPERAÇÃO SOLICITADA EM CADA CASO.

from time import sleep
opcao = 0
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
teste = False
while opcao != 5:
    print('-=' * 17)
    print('''Escolha entre as opções abaixo:
       [ 1 ] para SOMAR
       [ 2 ] para MULTIPLICAR
       [ 3 ] para MAIOR
       [ 4 ] para NOVOS NÚMEROS
       [ 5 ] para SAIR DO PROGRAMA''')
    opcao = int(input('Digite a sua opção: '))
    print('-=' * 17)
    if opcao == 1:
        print('A soma dos números {} + {} é {}'.format(n1, n2, (n1 + n2)))
    elif opcao == 2:
        print('A multiplicação de {} x {} é {}'.format(n1, n2, (n1 * n2)))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print('Entre {} e {} o maior é {}'.format(n1, n2, maior))
        elif n2 > n1:
            maior = n2
            print('Entre {} e {} o maior é {}'.format(n1, n2, maior))
        else:
            print('Os números são iguais.')
    elif opcao == 4:
        n1 = int(input('Digite um novo número: '))
        n2 = int(input('Digite outro novo número: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(1)
    else:
        print('Opção inválida. Tente novamente !!')
print('-=' * 17)
print('FIM DO PROGRAMA')