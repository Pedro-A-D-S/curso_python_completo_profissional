# importando módulo que manipula o sistema operacional
import os

# limpando a tela
os.system('cls') or None

# Entrada de dados

## recebe o primeiro número e guarda na variável num1
num1 = input('Digite o primeiro número: ')

## converte num1 para inteiro
num1 = int(num1)

## recebe o primeiro número e guarda na variável num1
num2 = input('Digite o segundo número: ')

## converte num2 para inteiro
num2 = int(num2)

# Processamento

## calcula o produto
produto = num1 * num2

# Saída da informação

## mensagem de saída do produto
print()
print('O produto entre', num1, 'e', num2, 'é', produto)