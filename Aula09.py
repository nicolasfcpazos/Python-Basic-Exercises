frase = 'Curso em Vídeo Python'

print(len(frase))
print(frase[3])   # mostra a 4a letra da string

print(frase[3:13])   # mostra a fatia da 4a letra até a 12a letra

print(frase[:13])   # mostra a fatia desde início (0) até a 12a letra

print(frase[3:13:2])   # mostra a fatia da 4a letra até a 12a letra, pulando de 2 em 2 letras

print(frase[1::2])   # mostra a fatia da 1a letra até o final, pulando de 2 em 2 letras

print(frase[::2])   # mostra a fatia desde o início até o final, pulando de 2 em 2 letras

print(frase.count('o'))   # conta quantas letras o, se encontra na frase

# EXEMPLO DE VISUALIZAÇÃO DE TEXTO GRANDE, USANDO 3 ASPAS NO INÍCIO E 3 NO FIM.
print('''Dezenas de simpatizantes se aglomeraram para 
ouvir o presidente, contrariando as orientações da de 
isolamento social da Organização Mundial da Saúde (OMS) 
para evitar a propagação do coronavírus. Durante o discurso, 
Bolsonaro tossiu algumas vezes, sem usar a parte interna do 
cotovelo, conforme orientação das autoridades sanitárias.''')
