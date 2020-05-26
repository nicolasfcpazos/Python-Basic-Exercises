# ESTRUTURA DE REPETIÇÃO

#for c in range(0, 6):
#    print(c)

#for c in range(6, 0, -1):   # CONTAGEM DE TRÁS PRA FRENTE
#    print(c)
#print('FIM')

#n = int(input('Digite um número: '))
#for c in range(0, n+1):
#    print(c)
#print('FIM')

# EXEMPLO
#i = int(input('Inicio: '))
#f = int(input('Fim: '))
#p = int(input('Passo: '))
#for c in range(i, f+1, p):
#    print(c)
#print('FIM')

s = 0
for c in range(0, 4):
    n = int(input('Digite um número: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))