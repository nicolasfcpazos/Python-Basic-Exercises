# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados
# moeda e dado.
# Transfira todos as funções utilizadas nos exercicios, 107, 108 e 109 para o
# primeiro pacote e mantenha tudo funcionando.


from Aula22_Ex111.utilidadescev import moeda


# Programa principal
print('-' * 30)
p = float(input('Digite o preço: R$ '))
moeda.resumo(p, 35, 22)
