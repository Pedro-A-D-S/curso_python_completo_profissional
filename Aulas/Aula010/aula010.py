# tipo de texto: str
# tipos numéricos: int, float, complex
# tipos de sequência: list, tuple, range
# tipo de mapeamento: dict
# tipos de conjuntos: set, frozenset
# tipo booleano: bool
# tipos binários: bytes, bytearray, memoryview

#### definit o tipo de dados ####

x = 'Hello World' # str
x = 20 # int
x = 20.5 # float
x = 1j # complex
x = ['apple', 'banana', 'cherry'] # list
x = ('apple', 'banana', 'cherry') # tuple
x = range(6) #range
x = {'name' : 'john', 'age' : '36'} # dict
x = {'apple', 'banana', 'cherry'} # set
x = frozenset({'apple', 'banana', 'cherry'}) # frozenset
x = True # bool
x = b'Hello' # bytes
x = bytearray(5) #bytearray

x = '20'
print(x)
print(type(x))

x = int('20')
print(type(x))