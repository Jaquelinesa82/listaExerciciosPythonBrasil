"""
Faça um programa que pergunte o preço de três produtos e informe qual produto
você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""

preco1 = float(input('Digite o valor do produto-1: '))
preco2 = float(input('Digite o valor do produro-2: '))
preco3 = float(input('Digite o valor do produto-3: '))

if (preco1 == preco2) and (preco1 == preco3):
    print('Valore iguais')
elif (preco1 < preco2) and (preco1 < preco3):
    print('produto-1: ', preco1)
elif (preco2 < preco3):
    print('produto-2: ', preco2)
else:
    print('produto-3: ', preco3)
