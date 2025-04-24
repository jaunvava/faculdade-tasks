'''
Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados:
valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo
'''

compra = float(input('digite o valor  sua compra:'))
print('valo da compra - juros - parcelas - valor da parcela')
print(f'{compra}    - {0}    - {1}    - {compra}')

juros = 10
 
for parcela in range(3, 13, 3):
        total = compra * (1 + juros / 100)
        valor_parcela = total / parcela 
        print(f'{total} - {juros} - {parcela} - {valor_parcela}')

        juros += 5