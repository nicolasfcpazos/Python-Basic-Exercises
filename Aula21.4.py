# Funções  - parte 2

# ESCOPO DE VARIÁVEIS

def teste():
    x = 8      # Variavel local, so existe dentro da função
    print(f'Na função teste, n vale {n}')
    print(f'NA função teste, x vale {x}')


# Programa principal
n = 2          # Variável global, existe dentro do programa geral
print(f'No programa principal, n vale {n}')
teste()
print(f'No programa principal, x valr {x}')   # Não vai funcionar



# Exemplo