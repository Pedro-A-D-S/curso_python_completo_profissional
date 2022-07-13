from re import X


x = 'incrível'
x = 'inacreditável'

def myFunc():
    y = 'fantástico'
    global z
    z = 'Bem vindo ao curso'
    print('Python é ' + x + ' e ' + y)

myFunc()

print('=============')
print('Você é ' + x)
print(z)