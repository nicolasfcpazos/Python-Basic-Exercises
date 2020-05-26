
def aumentar(preço=0, taxa=0, formato=False):
    """
    -> Calcula o percentual de aumento de um valor.
    :param preço: Valor a ser calculado.
    :param taxa: Percentual a ser aumentado no valor.
    :param formato: Se formata (opcional) o valor ou não.
    :return: Retona o valor aumentado.
    """
    res = preço + ((preço * taxa) / 100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    """
    -> Calcula o percentual de redução de um valor.
    :param preço: Valor a ser calculado.
    :param taxa: Percentual a ser reduzido no valor.
    :param formato: Se formata (opcional) o valor ou não.
    :return: Retorna o valor reduzido.
    """
    res = preço - ((preço * taxa) / 100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    """
    -> Calcula o dobro de um número.
    :param preço: Valor a ser calculado.
    :param formato: Se formata (opcional) o valor ou não.
    :return:  Retorna o dobro do número.
    """
    res = preço * 2
    return res if formato is False else moeda(res)


def metade(preço=0, formato=False):
    """
    -> Calcula a metade de um número.
    :param preço: Valor a ser calculado.
    :param formato: Se formata (opcional) o valor ou não.
    :return: Retorna a metade do número.
    """
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(preço=0, moeda='R$'):
    """
    -> Verifica se o número digitado é um valor e formata o mesmo
    :param preço: Número a ser verificado.
    :param moeda: Verifica se o o número é um valor e formata o mesmo.
    :return: Retorna o número formatado como moeda (formato BR com vírgula).
    """
    return f'{moeda} {preço:.2f}'.replace('.', ',')
