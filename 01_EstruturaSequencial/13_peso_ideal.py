"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um
algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7

"""
sexo = input('Digite o sexo (F/M): ')
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

if (sexo == '(F/M)'):
    pesoIdeal = ((72.7 * altura) - 58)
else:
    pesoIdeal = ((62.1 * altura) - 44.7)

if (peso < pesoIdeal):
    print('Você está acima do peso ideal', pesoIdeal)
elif(peso > pesoIdeal):
    print('Você está abaixo do peso.', pesoIdeal)
else:
    print('Você está no peso ideal.', pesoIdeal)
