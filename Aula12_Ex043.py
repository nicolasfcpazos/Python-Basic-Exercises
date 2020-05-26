#  DESENVOLVA UMA LÓGICA QUE LEIA O PESO E A ALTURA DE UMA PESSOA,
# CALCULE SEU IMC E MOSTRE SEU SATUS, DE ACORDO COM A TABELA ABAIXO:

# ABAIXO DE 18.5: ABAIXO DO PESO
# ENTRE 18.5 E 25: PESO IDEAL
# 25 ATÉ 30: SOBREPESO
# 30 ATÉ 40: OBESIDADE
# ACIMA DE 40: OBESIDADE MÓRBIDA

# FORMULA: PESO / (ALTURA X ALTURA)

import time

print('Vamos verificar seu IMC ?')
print('='*20)
peso = float(input('QUal o seu peso em KG ? '))
altura = float(input('Qual a sua altura ? '))
print('='*20)
print('Calculando...')
time.sleep(1)
print('')
imc = peso / (altura ** 2)

print('Seu IMC é {:.2f}.'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO.')
elif 18.5 <= imc < 25:
    print('Você está no PESO IDEAL.')
elif 25 <= imc < 38:
    print('Você está com SOBREPESO.')
elif 38 <= imc < 40:
    print('Você está com OBESIDADE.')
elif imc >= 40:
    print('Você está com OBESIDADE MÓRBIDA.')
