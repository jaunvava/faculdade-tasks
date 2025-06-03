# Escrevendo em um arquivo
with open('exemplo.txt', 'w') as arquivo:
    arquivo.write('Olá, mundo!\n')
    arquivo.write('Esta é uma segunda linha.\n')
    arquivo.write('Esta é uma terceira linha.\n')

# Lendo o conteúdo do arquivo
with open('exemplo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)