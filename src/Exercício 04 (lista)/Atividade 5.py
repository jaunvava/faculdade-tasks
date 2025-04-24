# construa um algoritmo que leia 5 nomes e verifique posteriormente se eles se repetem

pessoas = []

for i in range(5):
    nome = input('digite um nome:')
    pessoas.append(nome)
    for j in nome:
        if nome == nome:
            print('o nome',nome,'se repete')
        elif nome != nome:
            print('os nomes são diferentes')



