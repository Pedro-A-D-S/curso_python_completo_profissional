import os

os.system('cls')

# adicionando itens na lista

nomes = ['Gabriel', 'Danny', 'Arthur']

# método append - insere item no final da lista
nomes.append('João')

# mostrando lista alterada
print(nomes)

# método insert - insere item na lista no índice especificado
nomes.insert(1, 'Mário')

# mostrando lista alterada
print(nomes)

# método extend - cria uma extensão na lista com outra lsita pré existente cou qualquer objeto iterável (lista, dicionário)
## forma literal
nomes.extend(['Lucas', 'Matheus', 'Flávio'])

# mostrando lista alterada
print(nomes)

## como parâmetro
outraLista = ['Lucas', 'Matheus', 'Flávio']
nomes.extend(outraLista)

# mostrando lista alterada
print(nomes)