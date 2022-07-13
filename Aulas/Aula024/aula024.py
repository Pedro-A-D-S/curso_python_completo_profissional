import os

os.system('cls')

# operadores de identidade

x = ['apple', 'banana']
y = ['apple', 'banana']

z = x

print(x is z)
print(x is y)

# embora sejam objetos diferentes, eles possuem conteúdos iguais
print(x == y)

print(x is not z)
print(x is not y)

# objetos diferentes, mas possuem mesmo tipo e conteúdo
print(x != y)