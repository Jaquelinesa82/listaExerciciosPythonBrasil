"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
"""
valor_horas = float(input('Digite o valor ganho por horas: '))
horas_trab = float(input('O valor de horas trabalhadas no mês: '))

print('Salário do mês é {}.'.format(valor_horas*horas_trab))
