# ESCREVA UM PROGRAMA PARA APROVAR O EMPRÉSTIMO BANCÁRIO PARA A COMPRA DE
# UMA CASA. O PROGRAMA VAI PERGUNTAR O VALOR DA CASA, O SALÁRIO DO COMPRADOR
# E EM QUANTOS ANOS ELE VAI PAGAR.

# CALCULE O VALOR DA PRESTAÇÃO MENSAL, SABENDO QUE ELA NÃO PODE EXCEDER
# 30% DO SALÁRIO OU ENTÃO O EMPRÉSTIMO SERÁ NEGADO.

valor = float(input('QuaL o valor do imóvel a ser financiado ? R$ '))
salario = float(input('Qual o salário do comprador ? R$ '))
ano = int(input('Em quantos anos pretende financiar o imóvel ? '))

parcela = valor / (ano * 12)

print('')
print('Para pagar uma casa no valor de R$ {:.2f} em {} anos,'.format(valor, ano))
print('a prestação será de R$ {:.2f}'.format(parcela))
print('')
if parcela <= (salario * 0.3):
    print('Parabéns ! Seu empréstimo foi APROVADO.')
else:
    print('Seu empréstimo foi NEGADO !')
print('Obrigado pela visita a nossa agência.')