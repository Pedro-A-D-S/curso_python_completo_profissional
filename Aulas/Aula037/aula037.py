import os

os.system('cls')

# tuplas

tupla1 = ('Gabriel', 'Danny', 'Arthur', 'Beatriz', 'João')
print(tupla1)
print(tupla1[0])
print(tupla1[1])

# é possível acessar através da indexação negativa
print(tupla1[-1])
print(tupla1[-3])

# acessando intervalo de elementos (o último item é excluso)
print(tupla1[2:5])

# ao omitir o item inicial, a tupla é selecionada desde o início
print(tupla1[:5])

print(tupla1[2:])

# intervalo utilizando itens negativos
print(tupla1[-4:-1])

print('Danny' in tupla1)

if 'Thiago' in tupla1:
    print('Sim, contém.')
else:
    print('Não contém.')

