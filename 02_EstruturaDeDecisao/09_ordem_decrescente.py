"""
Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))

if num1 > num2 > num3:
    print(num1, num2, num3)
if num1 > num3 > num2:
    print(num1, num3, num2)
if num2 > num1 > num3:
    print(num2, num1, num3)
if num2 > num3 > num1:
    print(num2, num3, num1)
if num3 > num1 > num2:
    print(num3, num1, num2)
if num3 > num2 > num1:
    print(num3, num2, num1)
if num1 == num2 or num2 == num1 or num2 == num3:
    print('inválido')



