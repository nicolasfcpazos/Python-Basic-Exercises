# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem
# por extenso, de zero até vinte.

# Seu programa deverá ler um número pelo teclado (0 a 20) e mostrá-lo por extenso.


numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete',
           'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',
           'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
print('----  NÚMERO POR EXTENSO ----')
print('-' * 29)
while True:
    escolha = int(input('Digite um número entre 0 e 20: '))
    if 0 <= escolha <= 20:
        break
    print('Tente novamente. ', end ='')
print(f'O número digitado por extenso é {numeros[escolha]}')

