# FAÇA UM PROGRAMA QUE MOSTRE NA TELA UMA CONTAGEM REGRESSIVA PARA O ESTOURO
# DE FOGOS DE ARTIFÍCIO, INDO DE 10 ATÉ 0, COM UMA PAUSA DE 1 SEGUNDO ENTRE ELES.

from time import sleep

print('Contagem para o Ano Novo !')
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('FELIZ ANO NOVO !')
