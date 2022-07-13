# Valores Booleanos

print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
    print('Sim, {} é maior que {}.'.format(a, b))
elif b == a:
    print('{} é igual a {}'.format(a, b))
else:
    print('Não, {} não é maior que {}.'.format(a, b))

# Quase sempre, retornará verdadeiro
print(bool('Olá'))
print(bool(15))
print(bool(['Apple', 'Cherry', 'Banana']))

x = 0
y = ''

# Valores que serão retornados falsos (objetos vazios)
print(bool(x))
print(bool(y))

def myFunction():
    return True

print(myFunction())

if myFunction():
    print('Sim!')
else:
    print('Não!')

x = 200
print(isinstance(x, int))


