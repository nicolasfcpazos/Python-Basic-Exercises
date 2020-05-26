
# O MESMO PROFESSOR QUER SORTEAR A ORDEM DE APRESENTAÇÃO DE TRABALHO DOS ALUNOS.
# FAÇA UM PROGRAMA QUE AJUDE ELE, LENDO O NOME DELES E MOSTRANDO A ORDEM ESCOLHIDA.

import random
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))

lista = [a1, a2, a3, a4]

random.shuffle(lista)

print(' A ordem dos alunos será:')
print(lista)


