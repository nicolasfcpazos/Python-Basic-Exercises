
num = [2, 5, 9, 1]
num[2] = 3       # --> substitui o registro 2 pelo objeto 3
num.append(7)    # --> insere no fim da lista
num.insert(2, 2)

if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4.')

# num.pop(2)    # --> apaga o registro 2
#num.remove(2)
print(num)
print(f'Essa lista tem {len(num)} elementos.')
num.sort(reverse=True)
print(num)

