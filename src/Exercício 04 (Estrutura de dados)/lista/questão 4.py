# 4. Faça um Programa que leia um vetor de 10 caracteres, e diga quantas
# consoantes foram lidas. Imprima as consoantes.

nomes = []

for i in range(10):
    letra = input('digite um nome:')

contador = 0
for letra in nomes:
    if letra not in ['a', 'e', 'i', 'o', 'u']:
        contador += 1
    print(f'A quantidade de consoantes são:{letra}')