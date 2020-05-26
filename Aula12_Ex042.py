# REFAÇA O EXERCÍCIO 35 DOS TRIÂNGULOS, ACRESCENTANDO O RECURSO DE
# MOSTRAR QUE TIPO DE TRIÂNGULO SERÁ FORMADO:

# EQUILÁTERO: TODOS OS LADOS IGUAIS
# ISÓSCELES: DOIS LADOS IGUAIS
# ESCALENO: TODOS OS LADOS DIFERENTES

print('-' * 30)
print('Analisador de Triângulos !')
print('-' * 30)

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM FORMAR um Triângulo ', end='')
    if a == b == c:
        print('EQUILÁTERO.')
    elif a == b or b == c or a == c:
        print('ISÓSCELES.')
    elif a != b != c:
        print('ESCALENO.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um Triângulo.')