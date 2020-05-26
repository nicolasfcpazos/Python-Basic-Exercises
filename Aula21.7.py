# Funções  - parte 2


# RETORNO DE VALORES

'''def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 4)
somar(2, 2)
somar(6)'''


# opção 2  -  outra forma de fazer

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 4)
r2 = somar(2, 2)
r3 = somar(6)
print(f'Meus cálculos deram {r1}, {r2} e {r3}.')