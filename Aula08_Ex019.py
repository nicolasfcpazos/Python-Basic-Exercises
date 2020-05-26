
# UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA APAGAR O QUADRO.
# FAÇA UM PROGRAMA QUE AJUDE ELE, LENDO O NOME DELES E ESCREVENDO O NOME DO ESCOLHIDO

import random

aluno1 = str(input('Nome do aluno 1: '))
aluno2 = str(input('Nome do aluno 2: '))
aluno3 = str(input('Nome do aluno 3: '))
aluno4 = str(input('Nome do aluno 4: '))

lista = (aluno1, aluno2, aluno3, aluno4)

resultado = random.choice(lista)

print('O aluno que irá apagar o quadro é: {}'.format(resultado))