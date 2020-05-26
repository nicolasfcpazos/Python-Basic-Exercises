# Faça um programa que leia nome e média de um aluno, guardando também
# a situação em um dicionário. No final, mostre o conteúdo da estrura na tela.

#  Ex: Nome: Joaquim           --> A perguntar
#      Média de Joaquim: 4.5   --> A perguntar
#      Nome é igual a Joaquim
#      Média é igual a 4.5
#      Situação é igual a Reprovado   --> A calcular

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
print('-=' * 20)
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
for k, v in aluno.items():               # Mostra a chave e o conteúdo
    print(f'  - {k} é igual a {v}')
