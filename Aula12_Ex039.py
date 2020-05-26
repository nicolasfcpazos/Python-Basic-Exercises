# FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORMA,
# DE ACORDO COM SUA IDADE:

# SE ELE AINDA VAI SE ALISTAR NO SERVIÇO MILITAR.
# SE É A HORA DE SE ALISTAR.
# SE JÁ PASSOU DO TEMPO DO ALISTAMENTO.

# SEU PROGRAMA TAMBÉM DEVERÁ MOSTRAR O TEMPO QUE FALTA QUE PASSOU DO PRAZO.

from datetime import date

print('Alistamento militar !')
nascimento = int(input('Em que ano você nasceu: '))
sexo = input('Qual o seu sexo: ').lower()
ano = date.today().year
idade = ano - nascimento
print('')

if sexo == 'masculino':
    print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, ano))
    if idade == 18:
        print('Você está na idade de se alistar ! Aliste-se este ano')
    elif idade > 18:
        print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))
        print('Seu alistamento foi em {}.'.format(nascimento + 18))
    elif idade < 18:
        print('Você ainda não chegou na idade de se alistar. \nAinda faltam {} anos para o alistamento.'.format(18 - idade))
        print('Seu alistamento será em {}'.format(nascimento + 18))
else:
    print('Você é uma mulher. Não precisa se alistar !')
