
def aumentar(preço=0, taxa=0):
    """
    -> Calcula o percentual de aumento de um valor.
    :param n: Valor a ser calculado.
    :param x: Percentual a ser aumentado no valor.
    :return: Retona o valor aumentado.
    """
    res = preço + ((preço * taxa) / 100)
    return res


def diminuir(preço=0, taxa=0):
    """
    -> Calcula o percentual de redução de um valor.
    :param n: Valor a ser calculado.
    :param x: Percentual a ser reduzido no valor.
    :return: Retorna o valor reduzido.
    """
    res = preço - ((preço * taxa) / 100)
    return res


def dobro(preço=0):
    """
    -> Calcula o dobro de um número.
    :param n: Valor a ser calculado.
    :return: Retorna o dobro do número.
    """
    res = preço * 2
    return res


def metade(preço=0):
    """
    -> Calcula a metade de um número.
    :param n: Valor a ser calculado
    :return: Retorna a metade do número.
    """
    res = preço / 2
    return res


def moeda(preço=0, moeda='R$'):
    return f'{moeda} {preço:.2f}'.replace('.', ',')
