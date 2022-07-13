# Formato de strings

idade = 36
txt = 'Eu sou o Gabriel e tenho {} anos de idade.'

# o método format retorna uma cópia da string txt e substitui as chaves pelo valor da variável idade.
print(txt.format(idade))

quantidade = 3
item = 'bolo'
valor = 14.99
meuPedido = 'Eu quero {} pedaços de {} por {} reais.'

# É possível utilizar o método format para mais que uma variável.
print(meuPedido.format(quantidade, item, valor))

meuPedido2 = 'Eu quero pagar {2} reais pelos {0} pedaços de {1}.'
print(meuPedido2.format(quantidade, item, valor))

