# Crie um programa que tenha uma função fatorial() , que receba
# dois parâmetros: primeiro que indique o número a calcular e o
# outro chamado show , que será um valor lógico (opcional) indicando
# se será mostrado ou não na tela o processo de cálculo de fatorial.


def fatorial(n, show=False):
    """
    --> Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial do número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Programa principal
print('-' * 30)
print(fatorial(5, show=True))
print('-' * 30)
help(fatorial)