# Crie um programa que leia:
# nome, ano de nascimento, e carteira de trabalho e cadastre-os (com idade)
# em um dicionário se por acaso a CTPS for diferente de ZERO,
# o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se
# aposentar.
# OBS: aposentadoria com 35 anos de trabalho

# campos: nome, idade e ctps (não armazenar o ano de nascimento)

from datetime import date

cadastro = dict()

cadastro['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
cadastro['idade'] = date.today().year - nasc
cadastro['ctps'] = int(input('Carteira de Trabalho (0 se não tem): '))
if cadastro['ctps'] != 0:
    cadastro['contratação'] = int(input('Ano de contratação: '))
    cadastro['salario'] = float(input('Salário: R$ '))
    cadastro['aposentadoria'] = (cadastro['contratação'] + 35) - nasc
print('-=' * 20)
for k, v in cadastro.items():               # Mostra a chave e o conteúdo
    print(f'  - {k} tem o valor {v}')