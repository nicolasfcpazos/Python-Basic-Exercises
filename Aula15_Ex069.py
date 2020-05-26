# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou
# não continuar. No final, mostre:

# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

maioridade = 0
homens = 0
mulheres = 0

while True:
    print('-' * 23)
    print('  CADASTRE UMA PESSOA')
    print('-' * 23)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M ou F] ')).strip().upper()[0]
    print('-' * 23)
    if idade >= 18:
        maioridade += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Você quer continuar cadastrando ? [S ou N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 23)
print(f'Total de pessoas com mais de 18 anos: {maioridade}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulheres} mulheres com menos de 20 anos')

