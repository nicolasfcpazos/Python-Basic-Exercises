nome = input ('Qual é o seu nome? ')
print ('Prazer em te conhecer {} !' .format(nome))
print ('Prazer em te conhecer {:20} !' .format(nome)) #mostra os primeiros 20 caracteres
print ('Prazer em te conhecer {:>20} !' .format(nome)) #alinha a direita
print ('Prazer em te conhecer {:<20} !' .format(nome)) #alinha a esquerda
print ('Prazer em te conhecer {:^20} !' .format(nome)) #centralizado
print ('Prazer em te conhecer {:=^20}!' .format(nome)) #centralizado
