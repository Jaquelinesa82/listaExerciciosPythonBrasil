"""
Faça um Programa que leia três números e mostre o maior deles.
"""
num1 = float(input('Digite um número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

if (num1 == num2) and (num1 == num3):
    print('números iguais')
elif (num1 > num2) and (num1 > num3):
    print(num1, ': Maior')
elif (num2 > num3):
    print(num2, ':Maior')
else:
    print(num3, ':Maior')
