# Faça um programa que tenha uma função chamada contador() , que receba
# três parâmetros: inicio, fim e passo e realize a contagem.
# Seu programa tem que realizar três contagens através de uma função criada:

# a) De 1 até 10, de 1 em 1
# b) De 10 até 0, de 2 em 2
# c) Uma contagem personalizada

from time import sleep

def contador(i, f, p):
    if p < 0:       # Se passo digitado for numero negativo, transforma-o em negativo
        p *= -1
    if p == 0:      # Se o passo digitado for zero, será transforado em 1
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1)
    if i < f:
        cont = i              # Para contagem do menor para o maior
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p         # aumenta o contador
        print('FIM !')
    else:
        cont = i              # para contagem do maior para o menor
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p        # diminui do contador para fazer do maior para menor
        print('FIM !')


# Programa principaç
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem !')
ini = int(input('Início: '))
fi = int(input('Fim: '))
pa = int(input('Passo: '))
contador(ini, fi, pa)

