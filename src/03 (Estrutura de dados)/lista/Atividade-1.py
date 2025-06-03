'''
crie uma lista vazia e leia o nome de todos ps alunos da sala colocando cada nome 
dentro da lista. continue escrevendo até que seja digitando a palavra fim.
'''
alunos = []

while True:
    nome = input('Digite seu nome):')
    # Se o nome for 'fim', saia do loop
    if nome == 'fim':
        break

    alunos.append(nome)

print('Os alunos são:')
for i in range(len(nome)):
    print(alunos[i])     

