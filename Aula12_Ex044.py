# ELABORE UM PROGRAMA QUE CALCULE O VALOR A SER PAGO POR UM PRODUTO,
# CONSIDERANDO O SEU PREÇO NORMAL E CONDIÇÃO DE PAGAMENTO:

# À VISTA DINHEIRO / CHEQUE: 10% DE DESCONTO
# À VISTA NO CARTÃO: 5% DE DESCONTO
# EM ATÉ 2X NO CARTÃO: PREÇO NORMAL
# 3X OU NO CARTÃO: 20% DE JUROS

print('{:=^40}'.format(' LOJAS AMERICANAS '))
preco = float(input('Qual o preço das compras ? R$ '))
print('')
print('''Forma de pagamento:
[1] - À Vista dinheiro/cheque: 10% de desconto
[2] - Á vista no cartão: 5% de desconto
[3] - 2x no cartão: Preço sem desconto
[4] - 3x ou mais no cartão: Preço com 20% de juros''')
opcao = int(input('Digite a opção: '))
print('='*15)

if opcao == 1:
    total = preco * 0.90
elif opcao == 2:
    total = preco * 0.95
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = preco * 1.2
    parcelas = int(input('Em quantas parcelas ? '))
    valorparcela = total / parcelas
    print('=' * 15)
    print('Sua compra será parcela em {}x de R$ {:.2f} COM JUROS.'.format(parcelas, valorparcela))
else:
    total = preco
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente !')
print('Sua compra de {:.2f} vai custar {:.2f} no final. '.format(preco, total))

