# Função passando argumentos

def ola_usuario(nome, idade):
    print(f'Seu nome e {nome}, e sua idade e {idade}')
    
ola_usuario('jose')


def saudar_usuario2(nome, idade):
    ano = 2025 - idade
    print(f'Olá {nome}, seja bem vindo, você tem {idade} anos')
    print(f'Essa pessoa nasceu no ano {ano}')

nome = input('Digite seu nome:')
idade = int(input('Digite sua idade:'))

saudar_usuario2(nome, idade)