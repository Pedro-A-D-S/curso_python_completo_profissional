import os

os.system('cls')

# removendo itens de listas

nomes = ['Gabriel', 'Danny', 'Arthur', 'Marcos', 'Carlos']

# mostrando lista original
print(nomes)

# método remove - remove 1 item da lista

nomes.remove('Danny')

# mostrando lista alterada
print(nomes)

# método pop - remove 1 item da lista, especificando o índice, não o elemento
nomes.pop(0)

## para remover o último item da lista, pode-se especificar o último índice da lista
nomes.pop()

# mostrando lista alterada
print(nomes)

# palavra chave del - remove 1 item da lista a partir do índice (similar ao método pop)
del nomes[1]

# mostrando lista alterada
print(nomes)

# del também pode apagar a lista inteira
## del nomes

# método clear - remove todos os itens da lista
nomes.clear()

# mostrando lista vazia
print(nomes)





