 # LEIA QUANTO UMA PESSOA TEM NA CARTEIRA E CONVERTA PARA DÓLARES
 ## considere U$ 1,00 = R$ 3,27

real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 3.27
print('Com R$ {:.2f}, você pode comprar US$ {:.2f} '.format(real, dolar))



