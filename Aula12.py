nome = str(input('Qual é o seu nome ? '))
if nome == 'Nicolas':
    print('Que nome bonito.')
elif nome == 'Pedro' or nome == 'Maria' or nome =='João':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssia Juliana':
    print('Belo nome feminino !')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {} !'.format(nome))
