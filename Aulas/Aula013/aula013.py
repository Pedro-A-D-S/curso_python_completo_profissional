a = 'Gabriel'
b = 'Seja bem vindo'
c = '''Ciência de dados (em inglês: data science) é uma área interdisciplinar, 
localiza-se em uma interface entre a estatística e a ciência da computação, 
que utiliza o método científico; processos, algoritmos e sistemas, 
para extrair conhecimento e tomar decisões a partir de dados dos diversos tipos,
sendo eles ruidosos, nebulosos, estruturados ou não-estruturados.
'''

# print(d)

e = 'Olá Mundo'

# print(e[0])

# for x in 'Gabriel':
#     print(x)

# x = len(e)
# print(x)

txt = 'Seja bem vindo ao curso de Python.'

print('vindo' in txt)
print('carro' in txt)

if 'vindo' in txt:
    print("Sim, 'vindo' está presente.") 

elif 'vindo' not in txt:
    print("Não, 'vindo' não está presente.")
    
else:
    print('A palabra não está presente.')