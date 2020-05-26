print('\033[1;31;43mOlá, Mundo !\033[m')
print('\033[4;33;44mOlá, Mundo !\033[m')
print('\033[1;35;43mOlá, Mundo !\033[m')
print('\033[30;42mOlá, Mundo !\033[m')
print('\033[mOlá, Mundo !')   # formatação padrão do pythom
print('\033[7;30mOlá, Mundo !\033[m')
print(' ')
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m !!!'.format(a, b))
print(' ')

# OUTRO MODO DE FAZER
nome = 'Nicolas Pazos'
print('Olá ! Muito prazer, {}{}{} !!!'.format('\033[4;34m', nome, '\033[m'))

# MAIS OUTRA MANEIRA DE FAZER - CRIANDO BIBLIOTECA DE CORES

