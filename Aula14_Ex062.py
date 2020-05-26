# MELHOR O DESAFIO 61, PERGUNTANDO PARA O USUÁRIO SE ELE QUER MOSTRAR MAIS
# ALGUNS TERMOS. O PROGRAMA ENCERRA QUANDO ELE DISSER QUE QUER MOSTRAR 0 TERMOS.


from time import sleep

print('PROGRESSÃO ARITMÉTICA !')
print('-='*25)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
print('-='*25)
print('Calculando...')
sleep(1)
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} '.format(termo), end='-> ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostar a mais ? '))
print('-='*25)
print('Progressão finalizada com {} termos mostrados'.format(total))
