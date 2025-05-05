# uso do slice

nome = 'joao pedro da cruz'

nome_completo  = nome.split(' ')
print(nome)

iniciais = ''

for nome in nome_completo:
    if nome not in ['da','do','de']:
        iniciais += nome[0]

print(iniciais)
