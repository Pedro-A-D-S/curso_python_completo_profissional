import os

os.system('cls')

# juntar listas

# listas originais
list1 = ['a', 'b', 'c', 'd']
list2 = [1, 2, 3]

# nova lista a partir da junção das duas
list3 = list1 + list2

# mostra nova lista
print(list3)

# anexado elementos da lista 2 na lista 1
for x in list2:
    list1.append(x)

# mostra lista1
print(list1)

# método extend:

list2.extend(list1)

# mostra lista2
print(list2)



