import os

os.system('cls')

# iterando com loop nas listas

# criando lista
nomes = ['Gabriel', 'Danny', 'Arthur']

# loop for

for x in nomes:
    print(x)

print('Fim da execução.')

# loop for nos índices
for i in (range(len(nomes))):
    print(nomes[i])

# loop while
i = 0
while i < 3: # até chegar no índice 2
    print(nomes[i])
    i += 1

[print(x) for x in nomes] # list comprehension