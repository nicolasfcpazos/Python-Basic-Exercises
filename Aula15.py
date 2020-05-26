
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
#print('A soma vale {}'.format(s))   # MANEIRA ANTIGA DE MOSTRAR A VARIÁVEL
print(f'A soma vale {s}')     # NOVA MANEIRA DE DECLARAR UMA VARIÁVEL PARA VER



# exemplo 2

'''nome = 'José'
idade = 33
salario = 987.3
print(f'O {nome} tem {idade} anos e ganha R$ {salario:.2f}')'''

