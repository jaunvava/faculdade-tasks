novo = open('meusatletas.txt', 'r')
linhas = novo.readlines()
novo.close()

ind = linhas.index('jose\n')
linhas[ind] = 'carlos\n'

novo = open('meusatletas.txt', 'w')
for linha in linhas:
    novo.write(linha)
novo.close()