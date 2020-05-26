# Funções    -   empacotamento

# Exemplo 1
'''def contador(* num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM')
    print()


contador(5, 7, 3, 1, 4)
contador(8, 4, 7)
contador(5, 3, 2)'''

# Exemplo 2
def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')


contador(5, 7, 3, 1, 4)
contador(8, 4, 7)
contador(5, 3, 2)


print()

# Exemplo 3  -  somando valores
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)

