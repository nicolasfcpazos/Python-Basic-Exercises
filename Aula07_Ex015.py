# Qual a quantidade de Km rodados por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por KM rodado.

carro = float(input('Por quantos dias o carro foi alugado ? '))
distancia = float(input('Quantos Km foram rodados com o carro ? '))

total = (carro * 60.00) + (distancia * 0.15)

print('O total a pagar pelo aluguel do carro é R$ {:.2f}'.format(total))

