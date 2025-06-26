def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

numero = 5
print(f"Fatorial de {numero} é {fatorial(numero)}")