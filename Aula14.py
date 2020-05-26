# ESTRUTURA DE REPETIÇÃO ENQUANTO (WHILE)

# EXEMPLO 1

'''c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')'''

# EXEMPLO 2

'''r = 'S'
while r == 'S':
    n = int(input('Digite um número: '))
    r = str(input('Deseja continuar [S/N] ? ')).upper()
print('FIM')'''

# EXEMPLO 3   -   VERIFICAR QUANTOS NÚMERO SÃO PARES E QUANTOS SÃO ÍMPARES

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares'.format(par, impar))
