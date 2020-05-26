# DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTÂNCIA DE UMA VIAGEM EM KM.
# CALCULE O PREÇO DA PASSAGEM, COBRANDO R$ 0,50 POR KM PARA VIAGENS ATÉ 200 KM
# E R$ 0,45 PARA VIAGENS MAIS LONGAS.

distancia = float(input('Qual é a distância de sua viagem ? '))

# ALTERNATIVA DE CÁLCULO EM UM LINHA APENAS
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45

print('O preço da sua passagem será de R$ {:.2f}'.format(preco))
print('Tenha uma boa viagem !')


# MODO NORMAL DE FAZER A CONDIÇÃO

'''if distancia <= 200:
    preco = distancia * 0.50
    print('Você está prestes a começar a sua viagem de {:.2f} Km.'.format(distancia))
else:
    preco = distancia * 0.45
    print('Você está prestes a começar a sua viagem de {:.2f} Km.'.format(distancia))'''