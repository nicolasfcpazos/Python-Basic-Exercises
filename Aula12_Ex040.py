# CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE SUA
# MÉDIA, MOSTRANDO UMA MENSAGEM NO FINAL, DE ACORDO COM A MÉDIA ATINGIDA:

# mÉDIA ABAIXO DE 5.0: REPROVADO
# MÉDIA ENTRE 5.0 E 6.9: RECUPERAÇÃO
# MÉDIA 7.0 OU SUPERIOR: APROVADO

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if media < 5.0:
    print('Sua média é de {}. Você foi REPROVADO !'.format(media))
elif 7 > media >= 5.0:
    print('Sua média é de {}. Você está em RECUPERAÇÃO !'.format(media))
else:
    print('Sua média é de {}. Você foi APROVADO !'.format(media))
