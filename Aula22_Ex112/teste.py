# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo
# chamado dado. Crie uma função chamada leiadinheiro() que seja capaz de
# funcionar como a função input() , mas com uma validação de dados para
# aceitar apenas valores que sejam monetários.


from Aula22_Ex112.utilidadescev import moeda, dado


# Programa principal
print('-' * 30)
p = dado.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(p, 35, 22)
