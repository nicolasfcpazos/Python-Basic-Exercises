# Funções  - parte 2

# FUNÇÕES OPCIONAIS


def somar(a, b, c=0):
    """
    Faz a soma de três valores e mostra o resultado na tela
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor (se existir)
    :return:
    Função criada por Nicolas Pazos
    """
    s = a + b + c
    print(f'A soma vale {s}')


somar(8, 4, 2)
somar(8, 4)     # Se C não receber nenhum valor, o sistema
                # irá considerar a variavel recebendo ZERO
help(somar)