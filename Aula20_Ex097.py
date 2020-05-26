# Faça um programa que tenha uma função chamada escreva() , que receba um
# texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

#  Ex:    escreva('Ola, Mundo!')
#  Resp:  -------------
#          Olá, Mundo!
#         -------------


def escreva(msg):
        tam = len(msg) + 4
        print('-' * tam)
        print(f'  {msg}')
        print('-' * tam)


# Programa principal
escreva('Nicolas')
escreva('Curso de Python no youtube')
escreva('Curso em Vídeo')

