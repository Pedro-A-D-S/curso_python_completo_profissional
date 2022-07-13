import os

os.system('cls')

# acessando itens da lista

# criando lista
lista = ['Gabriel', 'Danny', 'Arthur', 'Gloria', 'Beatriz', 'Flávio']

# printando o item no índice 1
print(lista[1])

# outra forma de mostrar o item do item 1
nome = lista[1]
print(nome)

# a indexação no python também pode ser negativa
print(lista[-1])

# acessando os itens de índice 2 a 4 (o último item é excluso)
print(lista[2:5])

# mostrando o primeiro item até o 4
print(lista[:5])

# mostrando a partir do item 3, até o último
print(lista[3:])

# verificando se determinado item está na lista
if 'Arthur' in lista:
    print('Sim, Arthur está na lista.')
else:
    print('Não, Arthus não está na lista.')
