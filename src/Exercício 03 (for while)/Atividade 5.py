# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento
# iniciais. Valide a entrada e permita repetir a operação.

pop_A = int(input('qual'))
tax_A float(input('digite a taxa de crescin=mento A:'))
tax_A = 1 + tax_A/100

pop_B = int(input('qual'))
tax_B float(input('digite a taxa de crescin=mento A:'))
tax_B= 1 +

taxa_A = 0.03  # 3%
taxa_B = 0.015  # 1.5%

anos = 0


while populacao_A < populacao_B:
    populacao_A *= (1 + taxa_A)
    populacao_B *= (1 + taxa_B)
    anos += 1

print(f"Serão necessários {anos} anos para a população do país A ultrapassar ou igualar a do país B.")
print(f"População final de A: {int(populacao_A):,} habitantes")
print(f"População final de B: {int(populacao_B):,} habitantes")