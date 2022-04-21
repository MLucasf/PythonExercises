'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite
a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
'''

while True:
    login=str(input("Login: "))
    senha=str(input("Senha: "))
    if login==senha:
        print("Senha inválida. A senha não pode ser igual ao login")
    else:
        print("Bem vindo!")
        break
