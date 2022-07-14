import os

os.system('cls')

# tuplas

tupla = ('Gabriel', 'Danny', 'Arthur', 'Danny')
print(tupla)
tam = len(tupla)
print(tam)

# criando tupla de 1 item: precisa colocar uma vírgula para que o Python reconheça cmo tupla
tupla2 = ('Carro',) # tupla de 1 item
print(type(tupla2))

tupla3 = ('Carro') # não é tupla
print(type(tupla3)) 

# as tuplas podem ter qualquer tipo de dado
tupla4 = (1, 5, 4, 25)
tupla5 = (False, False, False)
tupla6 = ('Gabriel', 36, '36', 1.65, True)

tupla7 = tuple(('Maçã', 'Laranja', 2021, '132', 'banana'))
print(tupla7)
print(type(tupla7))