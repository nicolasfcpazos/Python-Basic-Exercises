# CRIE UM PROGRAMA QUE LEIA UMA FRASE QUALQUER E DIGA SE ELA É UM PALINDROMO,
# DESCONSIDERANDO OS ESPAÇOS.

print('VERIFICADOR DE PALAVRAS PALÍNDROMAS')
print('-='*20)
frase = str(input('Escreva uma frase: ')).upper().strip()
palavras = frase.split()    #tira os espaçcos do inicio e do fim da frase
junto = ''.join(palavras)   #junta as frases sem espaço entre elas
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um Palíndromo !')
else:
    print('A frase digitada não é um Palíndromo !')


# Outra maneira de transformar a frase ao contrário
'''inverso = ''
for letra in range(len(junto) - 1, -1, -1):   # DA ÚLTIMA LETRA ATÉ A PRIMEIRA LETRA DA FRASE
    inverso += junto[letra]'''