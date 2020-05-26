# LISTAS - PARTE 2

teste = list()
teste.append('Nicolas')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(teste)
print(galera)

print('-=' * 30)

# Outro exemplo

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)
print(galera[0])  # Mostra apenas os dados do João
print(galera[2][1])  # Mostra apenas a idade do Joaquim
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')
    print(p)  # Motra o nome e a idade de cada pessoa
    print(p[0])  # Motra o nome de cada pessoa
    print(p[1])  # Motra a idade de cada pessoa