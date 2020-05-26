# Faça um algoritmo que leia o salário de uma pessoa e mostre seu novo salário, acrescido de 15%

salario = float(input('Qual é o salário do funcionário? R$ '))
salarionovo = float(salario * 1.15)
print('O funcionário que ganhava R$ {:.2f}, com 15% de aumento, passará a ganhar R$ {:.2f}'.format(salario, salarionovo))


