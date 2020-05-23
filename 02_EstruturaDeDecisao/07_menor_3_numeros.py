"""
Faça um Programa que leia três números e mostre o maior e o menor deles.
"""
num1 = int(input('Digite um número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

if (num1 == num2) and (num1 == num3):
    print('Números iguais')
else:
    if (num1 > num2) and (num1 > num3):
        print(num1, 'Maior')
    elif (num2 > num3):
        print(num2, 'Maior')
    else:
        print(num3, 'Maior')

    if(num1 < num2) and (num1 < num3):
        print(num1, 'Menor')
    elif (num2 < num3):
        print(num2, 'Menor')
    else:
        print(num3, 'Menor')
