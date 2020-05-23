"""
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
"""
valor = int(input('Digite um valor: '))

if (valor > 0):
    print(valor, ': Positivo')
elif (valor < 0):
    print(valor, ': Negativo')
else:
    print('Valor e igual a 0')
