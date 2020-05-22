"""
Faça um Programa que peça a temperatura em graus Celsius,
transforme e mostre em graus Farenheit.
"""
graus_C = float(input('Digite uma temperatura em Celsius : '))
print('A temperatura em graus Farenheit é {}.'.format(((graus_C / 5.0) * 9.0) + 32.0))
