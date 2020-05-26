# CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:

# O NOME COM TODAS AS LETRAS MAIÚSCULAS.
# O NOME COM TODAS MINÚSCULAS.
# QUANTAS LETRAS AO_TODO (SEM CONDIDERAR ESPAÇOS).
# QUANTAS LETRAS TEM O PRIMEIRO NOME.

nome = str(input('Digite o seu nome completo: ')).strip()

print('Seu nome todo em letra maiúscula é: ', nome.upper())
print('Seu nome todo em letra minúscula é: ', nome.lower())
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))


