"""
Faça um programa que leia um nome de usuário e a sua senha
e não aceite a senha igual ao nome do usuário, mostrando uma
mensagem de erro e voltando a pedir as informações.
"""
login = senha = ''

while (login == senha):
    login = input('Digite seu nome de usúario: ')
    senha = input('Digite sua senha: ')
    if(login == senha):
        print('A senha nao pode ser igual ao nome do usuario')
else:
    print('Cadastro realizado!')



