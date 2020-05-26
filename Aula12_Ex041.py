# A CONFEDERAÇÃO NACIONAL DE NATAÇÃO PRECISA DE UM PROGARAMA QUE LEIA
# O ANO DE NASCIMENTO DE UM ATLETA E MOSTRA SUA CATEGORIA, DE ACORDO COM
# A IDADE:

# ATÉ 9 ANOS: MIRIM
# ATÉ 14 ANOS: INFANTIL
# ATÉ 19 ANOS: JUNIOR
# ATÉ 25 ANOS: SÊNIOR
# ACIMA: MASTER

from datetime import date
ano = date.today().year
nasc = int(input('Em que ano o atleta nasceu: '))
idade = ano - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM.'.format(idade))
elif idade <= 14:
    print('Classificação: INFANTIL.'.format(idade))
elif idade <= 19:
    print('Classificação: JÚNIOR.'.format(idade))
elif idade <= 25:
    print('Classificação: SÊNIOR.'.format(idade))
else:
    print('Classificação: MASTER.'.format(idade))

