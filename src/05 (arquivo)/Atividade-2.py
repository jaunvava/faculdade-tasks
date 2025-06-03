
atletas = []

def inserir_arquivo(nome):
    file = open('meusatletas.txt', 'a')
    file.write(nome + '\n')
    file.close()

op = 9
inserir_arquivo('Esses são meus atletas:')

while op != 0:
    print('--- MENU ---')
    print('1. Inserir atleta:')
    print('2. Remover atleta:')
    print('3. Salvar lista atletas em arquivo:')

    op = int(input('Digite a opcao desejada:'))

    if op == 1:
        nome = input('Digite seu nome:')
        atletas.append(nome)
        inserir_arquivo(nome)

    elif op == 2:
        nome = input('Digite o nome para remover:')
        if nome in atletas:
            atletas.remove(nome)

    elif op == 3:
        file = open('meusatletas.txt','w')
        file.write('Esses são nossos atletas queridos:\n')
        for nome in atletas:
            file.write(nome + '\n')
        file.close()












