# FAÇA UM PROGRAMA QUE LEIA O PESO DE CINCO PESSOAS. NO FINAL, MOSTRE QUAL FOI O
# MAIOR E O MENOR PESO LIDOS.


maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Digite o peso da {}a pessoa (em Kg): '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é {:.2f} Kg'.format(maior))
print('E o menor peso é {:.2f} Kg'.format(menor))
