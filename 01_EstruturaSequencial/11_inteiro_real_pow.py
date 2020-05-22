"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro mais metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
"""
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro:'))
num3 = float(input('Digite um número real: '))
prod = (2 * num1) + (2 / num2)
soma = (3 * num1) + num3
num3 = num3 ** 3

print('produto é: {} e a soma: {}, ao cubo é: {}.'.format(prod, soma, num3))

