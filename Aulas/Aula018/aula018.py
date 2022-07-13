# caracteres de escape

txt = "Somos os chamados \"vikings\" do norte."
print(txt)
txt = 'Ola\nMundo!'
print(txt)
txt = 'Ola\rMundo!'
print(txt)
txt = 'Ola\tMundo!'
print(txt)
txt = 'Isso irá inserir um \\ (barra invertida).'
print(txt)
txt = 'It\'s alright.'
print(txt)

# Este exemplo apaga um caracter (backspace):
txt = 'Ola \bMundo!'
print(txt)
# Uma barra invertida seguida por um 'x' é um número hexadecimal
txt = '\x48\x65\x6c\x6c\x6f'
print(txt)
# Uma barra invertida seguida por três inteiros resultará em um número octal
txt = '\110\145\154\154\157'
print(txt)
