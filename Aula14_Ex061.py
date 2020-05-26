# REFAÇA O DESAFIO 051, LENDO O PRIMEIRO TERMO E A RAZÃO DE UMA PA (PROGRESSÃO ARITMÉTICA),
# MOSTRANDO OS 10 PRIMEIROS TERMOS DA PROGRESSÃO USANDO A ESTRUTURA WHILE.


from time import sleep

print('10 PRIMEIROS TERMOS DE PROGRESSÃO ARITMÉTICA !')
print('-='*25)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
print('-='*25)
print('Calculando...')
sleep(1)
termo = primeiro
cont = 1
while cont <= 10:
    print('{} '.format(termo), end= '-> ')
    termo += razao
    cont += 1
print('FIM')
