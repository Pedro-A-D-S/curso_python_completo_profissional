a = 'Gabriel Artigas'

# retorna uma cópia da string com todas as letras maiúsculas 
b = a.upper()

print(b)

# retorna uma cópia da string com todas as letras maísculas
c = a.lower()

print(c)

d = '   Gabriel Artigas         '
print('>' + d + '<')

# retorna uma cópia da string sem espaçamentos no começo e no final
e = d.strip()

print(e)

# substitui uma parte da string por outra

f = a.replace('Artigas', 'Maciel')
print(f)

# retorna uma lista entre as partes separadas da string

g = 'Carro, Moto, Caminhão'
h = g.split(',')
print(h)
