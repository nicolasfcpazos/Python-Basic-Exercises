# FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA, MOSTRANDO EM SEGUIDA
#  O PRIMEIRO E O ÚLTIMO NOME SEPARADAMENTE.

#EXEMPLO: Ana Maria de Souza
# primeiro: Ana
# último: Souza

n = str(input('Digite um nome completo: ')).strip()

nome = n.split()

print('O primeiro nome é: {}'.format(nome[0]))
print('O último nome é: {}'.format(nome[len(nome)-1]))
