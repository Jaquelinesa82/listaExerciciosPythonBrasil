"""
Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))
if (num1 == num2) or (num1 == num3) or (num2 == num3):
    print('Números inválidos ou números iguais')
elif (num1 > num2) and (num1 > num3):
    print(num1)
    if (num2 > num3):
        print(num2)
        print(num3)
    else:
        print(num3)
        print(num2)
elif (num2 > num3):
    print(num2)
    if (num1 > num3):
        print(num1)
        print(num3)
    else:
        print(num3)
        print(num1)
else:
    print(num3)
    if (num1 > num2):
        print(num1)
        print(num2)
    else:
        print(num2)
        print(num1)





