# FAÇA UM PROGRAMA QUE PERGUNTE O SALÁRIO DE UM FUNCIONÁRIO E CALCULE O VALOR
# DO SEU AUMENTO.
# PARA SALÁRIOS SUPERIORES A R$ 1.250,00, CALCULE UM AUMENTO DE 10%.
# PARA OS INFERIORES OU IGUAIS, O AUMENTO É DE 15%.

salario = float(input('QUal o salaŕio do funcionário: R$ '))
if salario <= 1250.00:
    salarionovo = salario * 1.15
    print('O salário do funcionário teve um aumento de 15%.')
else:
    salarionovo = salario * 1.10
    print('O salário do funcionário teve um aumento de 10%.')
print('Quem ganhava R$ {:.2f}, passará a ganhar R$ {:.2f}'.format(salario, salarionovo))
