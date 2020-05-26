# Funções  - parte 2

# ESCOPO DE VARIÁVEIS


def teste(b):
    global a       # Utiliza a variavel global (programa principal)
    a = 8
    b += 4         # variaval recebe valor global de A e adiciona 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


# Programa principal
a = 5
teste(a)
print(f'A fora vale {a}')  # pega o valor dentro da definição
                           # por utiliza o comando global


