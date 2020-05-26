# FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DE TRÊS RETAS E DIGA AO USUÁRIO
# SE ELAS PODEM OU NÃO FORMAR UM TRIÂNGULO.


print('-' * 30)
print('Analisador de Triângulos !')
print('-' * 30)

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a < b + c and b < a + c and c < a + b:
    print('Os segumentos acima PODEM FORMAM um Triângulo.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um Triângulo.')


# OUTRA MANEIRA DE CALCULAR
#if (a - b) < c < (a + c) and (a - c) < b < (a + c) and (c - b) < a < (c + b):

# Para construir um triângulo é necessário que a
# medida de qualquer um dos lados seja menor que
# a soma das medidas dos outros dois e maior que
# o valor absoluto da diferença entre essas medidas.
