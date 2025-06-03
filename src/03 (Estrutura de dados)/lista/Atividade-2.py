# crie um sistema de voto que contabilise x votos para 3 candidatos, são 3400 eleitores
# e imprima o resultado final



candidatos = ['jose', 'maria', 'carlos']
votos = [0, 0, 0]

voto = 0

for i in range(3400):
    for j in range(len(candidatos)):
        print(f'{j + 1} - {candidatos[j]}')
    voto = int(input('Digite o número do candidato:'))

    voto[voto -1 ] += 1 



if votos[0] > voto[1] and voto[0] > voto[2]:
    print('quem ganhou a eleição foi:', candidatos[0])

elif votos[1] > voto[0] and voto[1] > voto[2]:
    print('quem ganhou a eleição foi:', candidatos[0])

elif votos[2] > voto[0] and voto[2] > voto[1]:
    print('quem ganhou a eleição foi:', candidatos[0])
    