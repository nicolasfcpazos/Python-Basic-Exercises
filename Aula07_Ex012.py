# Faça um algoritmo que leia o preço de um produto e mostre seu nov preço, com 5% de desconto

valor = float(input('Qual o valor do produto? R$ '))
desconto = float(input('Qual o % de desconto ? '))
novo = valor - (valor * desconto / 100)
print('O produto que custava R$ {:.2f}, com desconto de {:.2f}%, fica no valor de R$ {:.2f}'.format(valor, desconto, novo))
