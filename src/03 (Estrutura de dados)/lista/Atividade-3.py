'''
crie uma lista e adicione 3 nomes dentro da lista, percorra a lista verificando se o nome inicia
com a lentra a, letra m, se sim, exiba.
'''

nomes = []

nomes.append('joao')
nomes.append('maria')
nomes.append('carlos')
nomes.append('amanda')

for nome in nomes:
    if nome[0] == 'm':
        print(nome)
    elif nome[0] == 'a':
        print(nome)


#         usando set
#         nomes = ['joao', 'maria', 'carlos', 'amanda']
#         letras_alvo = {'a', 'm'}
#
#         nomes_filtrados = [nome for nome in nomes if nome[0].lower() in letras_alvo]
#         for nome in nomes_filtrados:
#             print(nome)