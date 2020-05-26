# Faça um programa que tenha a função leiaint() , que vai funcionar
# de forma semelhante à função input() do python, só que fazendo a
# validação para aceitar apenas um valor numérico.

#EX:   n = leiaint('Digite um n')


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))     # Mostra a msg p inserir o dado
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO ! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


#Programa Principal
print('-' * 30)
n = leiaInt('Digite um número: ')
print(f'Voce acabou de digitar o número {n}')