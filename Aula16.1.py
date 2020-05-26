
# TUPLAS

# EXEMPLO 1

lanche = ('Hambuguer', 'Suco', 'Pizza', 'Pudim')
print(sorted(lanche))   #--> ORGANIZA OS ELEMENTOS EM ORDEM alfabética
print(lanche)


# EXEMPLO 2
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a     # JUNTA AS TUPLAS A E B
print(c)
print(c.count(5))   # CONTAS QUANTAS VEZES APARECE O NUMERO 5 NA TUPLA - RESPOSTA: 2 VEZES
print(c.index(8))   # MOSTRA EM QUE POSIÇÃO O 8 APARECE - RESPOSTA: POSIÇÃO 1
print(c.index(2))   # MOSTRA EM QUE POSIÇÃO O 2 APARECE - RESPOSTA: POSIÇÃO 3 (MOSTRA A PRIMEIRA QUE APARECE)
print(c.index(5, 1)) # Procura o número 5, iniciando na posição 1 e mostra que aparece na 5a posição

# EXEMPLO 3
pessoa = ('Nicolas', 40, 'M', 118.30)
print(pessoa)

# del(pessoa)   -- Pode se usar para apagara uma tupla
