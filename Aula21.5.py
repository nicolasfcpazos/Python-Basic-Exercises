# Funções  - parte 2

# ESCOPO DE VARIÁVEIS

# Pode-se utilizar nomes de variaveis iguais dentro e fora do escopo

def funcao():    # escopo função
    n1 = 4       # Variavel local, so existe dentro da função
    print(f'N1 dentro vale {n1}')


# Programa principal    # escopo globaç
n1 = 2          # Variável global, existe dentro do programa geral
funcao()
print(f'N1 fora vale {n1}')