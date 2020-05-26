
def leiaDinheiro(msg):    # verifica se o valor informado é valor(dinheiro)
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)


def leiaInt(msg):     # verifica se o valor informado é um número inteiro
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