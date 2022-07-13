import os

os.system('cls')

# list comprehension

# lista original
nomes = ['Gabriel', 'Danny', 'Arthur', 'João', 'Lucas']

# queremos selecionar apenas os nomes com a letra u

# sem list comprehension

novaLista = []
for x in nomes:
    if 'u' in nomes:
        novaLista.append(x)

# mostrando nova lista
print(novaLista)

# utilizando list comprehension
novaLista1 = [x for x in nomes if 'u' in x]

# mostrando nova lista
print(novaLista1)

novaLista2 = [x for x in nomes if x != 'Danny']

# mostrando nova lista
print(novaLista2)

novaLista3 = [x for x in range(10) if x % 2 == 0]

# mostrando nova lista
print(novaLista3)

# criando lista com números ímpares sem list comprehension
X_impares = []
for x in range(10):
    if x % 2 != 0:
        X_impares.append(x)

print(X_impares)

# números ímpares com list comprehension
X_impares_lc = [x for x in range(10) if x % 2 != 0]
print(X_impares_lc)

# alterando valores na lista com list comprehension
novaLista_danny_lc = [x if x != 'Danny' else 'Danielle' for x in nomes]

print(novaLista_danny_lc)
