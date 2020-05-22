"""
Faça um Programa que peça a temperatura em graus Farenheit,
transforme e mostre a temperatura em graus Celsius.
C = (5 * (F-32) / 9).
"""
graus_F = float(input('Digite a temperatura Farenheit: '))

print('A temperatura em graus Celsius é: {} .'.format((5 * (graus_F-32) / 9)))
