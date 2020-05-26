frase = 'Curso em Vídeo Python'

print('Curso' in frase) #Verifica se a palavra Curso existe dentro da frase. Se sim, True.

print(frase.find('Curso')) #Verifica se a palavra existe na frase, se sim, mostra onde começa

print(frase.lower().find('vídeo')) # Muda a frase para minísculo e busca a palavra.

print(frase.split()) #Divide a frase e coloca as palavras em uma lista

dividido = frase.split()  #Cria uma lista com as palavras da frase
print(dividido[2][3])   #Mostra o 2o objeto e mostra a 3a letra



