'''
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e
que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e
escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B,
mantidas as taxas de crescimento.
'''


paisA = 80000
paisB = 200000

taxa_a = 3
taxa_b = 1.5
anos = 0

while paisB < paisA:
    anos += 1
    paisA = paisA * 1.03
    paisB = paisB * 1.015
    print(f'Pais a {paisA} - pais b {paisB}')

print(f'levou {anos} anos para A superar ou igualar B')




