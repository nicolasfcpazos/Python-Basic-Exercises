# TRATAMENTO DE ERROS E EXCEÇÕES

# EXEMPLO 1
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:   # Exemplo de tratamento de erro mostrando o erro
    print(f'Problema encontrado foi: {erro.__class__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre ! Muito obrigado')


