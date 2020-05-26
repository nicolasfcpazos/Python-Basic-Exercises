# Crie um código em Python que teste se o site Pudim está acessivel pelo
# computador usado.


import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.interativadoc.com.br')
except urllib.error.URLError:
    print('O site da INTERATIVA não está acessível no momento !')
else:
    print('Consegui acessar o site DA INTERATIVA com sucesso')
    print(site.read())
