# LEIA UM VALOR EM METROS E EXIBA CONVERTIDO EM CENTIMENTOS E MILIMETROS

n = int(input('Digite um valor em metros '))
dm = n * 10
cm = n * 100
mm = n * 1000
km = n / 1000
hm = n / 100
dam = n / 10
print('O valor {} m é de: ')
print('Em decímetros é: {} decimetros'.format(dm))
print('Em centimentros é: {} centímetros'.format(cm))
print('Em milimetros é: {} milimetros'.format(mm))
print('Em decametros é: {} decâmetros'.format(dam))
print('Em hectômetros: {} hectômetros'.format(hm))
print('Em quilômetros é {} quilômetros'.format(km))
