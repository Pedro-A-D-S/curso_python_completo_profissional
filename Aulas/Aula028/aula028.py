import os

os.system('cls')

# alterando itens na lista

nomes = ['Gabriel', 'Danny', 'Arthur', 'João']
print(nomes)

# alterando item da lista que se encontra no índice 1
nomes[1] = 'Danielle'

# printando lista com item alterado
print(nomes)

# alterando a lista dentro de range
nomes[1:3] = ['Glória', 'Beatriz']

# printando lista com item alterado
print(nomes)

# caso seja inserido mais itens que aquele que foi especificado inicialmente, o número da lista será aumentado

# alterando a lista dentro de range
nomes[1:3] = ['Glória', 'Beatriz', 'Flávio', 'Lucas']

# printando lista com item alterado
print(nomes)

# caso não seja inserido o número total de itens especificado no range, então o item entrará no intervalo inteiro

# alterando a lista dentro de range
nomes[1:3] = ['Lucas']

# printando lista com item alterado
print(nomes)

# método insert

# lista original
nomes = ['Gabriel', 'Danny', 'Arthur', 'João']

# inserindo antes do índice já existente
nomes.insert(2, 'Mario')

# printando lista com item alterado
print(nomes)