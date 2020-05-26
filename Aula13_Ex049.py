# REFAÇA O EXERCÍCIO 9, TABUADA, MOSTRANDO A TABUADA DE UM NÚMERO QUE O USUÁRIO
# ESCOLHER, SÓ QUE AGORA UTILIZANDO UM LAÇO FOR.


n = int(input('Digite um número para ver sua tabuada: '))
for c in range (1, 11):
    print('{} x {:2} = {}'.format(n, c, n*c))
print('FIM')