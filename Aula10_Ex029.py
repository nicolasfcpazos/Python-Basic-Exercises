# ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO.
# SE ELE ULTRAPASSAR 80 KM/H, MOSTRE UMA MENSAGEM DIZENDO QUE FOI MULTADO.
# A MULTA VAI CUSTAR R$ 7,00 PARA CADA KM ACIMA DO LIMITE.

velocidade = float(input('Qual é a velocidade atual do carro: '))

if velocidade > 80:
    print('Multado ! Você está acima limite de velocidade que é de 80 Km/h')
    multa = (velocidade - 80) * 7
    print('O valor da sua multa é de R$: {:.2f}'.format(multa))
print('Tenha um bom dia. Dirija com segurança')

