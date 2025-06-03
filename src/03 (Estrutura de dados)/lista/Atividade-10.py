# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

reais = []
for i in range(5):
    num = float(input('digite um numero real:'))
    reais.append(num)

for j in range(len(reais) -1, -1, -1):
    print(reais[j], end='-')


