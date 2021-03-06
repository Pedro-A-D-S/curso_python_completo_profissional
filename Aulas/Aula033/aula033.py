import os

os.system('cls')

# classificação de lista

nomes = ['Gabriel', 'Danny', 'Arthur', 'João', 'Beatriz']

numeros = [100, 50, 82, 23]

# método sort

nomes.sort()
numeros.sort()

print(nomes)
print(numeros)

nomes.sort(reverse = True) # ordem decrescente
numeros.sort(reverse = True) # ordem decrescente

print(nomes)
print(numeros)

def myfunction(n):
    return abs(n - 50)

numeros.sort(key = myfunction)

print(numeros)

# classificar sem a distinção de maiúsculo e minúsculo
nomes.sort(key = str.lower)

print(nomes)

# inverter a ordem dos itens na lista
nomes.reverse()
numeros.reverse()

print(nomes)
print(numeros)

