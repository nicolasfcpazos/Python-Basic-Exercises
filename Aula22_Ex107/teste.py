# Crie um módulo chamado moeda.py que tenha as funções incorporadas
# aumentar() , diminuir() , dobro() e metade() .
# Faça também um programa que importe esse módulo e use algumas dessas funções.


from Aula22_Ex107 import moeda

# Programa principal
p = float(input('Digite o preço: R$ '))
print('-' * 40)
print(f'A metade de R$ {p} é R$ {moeda.metade(p)}')
print(f'O dobro de R$ {p} é R$ {moeda.dobro(p)}')
print(f'Aumentando 10%, temos R$ {moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos R$ {moeda.diminuir(p, 13)}')
