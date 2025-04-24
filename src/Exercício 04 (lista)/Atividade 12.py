alunos = []

op = 99

while op != 0:
    print('----MENU----')
    print('1-Cadastrar usuario:')
    print('2-Remover usuario:')
    print('3-Listar alunos:')
    print('4-Buscar nome:')
    print('5-Médias do aluno:')
    print('6-Atualizar dados do aluno:')

    op = int(input('digite a opcao desejada '))

# 1 funcionalidade
    if op == 1:
        nome = input('digite seu nome')
        mat = input('digite a matricula')
        curso = input('digite seu curso')
        mens = float(input('digite o valor da mensalidade'))

        alunos.append([nome, mat, curso, mens])
        print('aluno cadastrado com sucesso \n')

# 2 funcionalidade
    elif op == 2:
        mat_remov = input('digite a matricula do aluno para remover ')
        indice = -1
        for i in range(len(alunos)):
            if mat_remov == alunos[i][1]:
                indice = i
        if indice != -1:
            alunos.pop(indice)
            print('aluno removido com sucesso')
        else:
            print('matricula nao encontrada')
    elif op == 3:
        for aluno in alunos:
            print(aluno)

# 4 funcionalidade
    elif op == 4:
        nome_busca = input('digite o nome para busca ')
        for aluno in alunos:
            if nome_busca == aluno[0]:
                print(f'Nome: {aluno[0]}')
                print(f'Matricula: {aluno[1]}')
                print(f'Curso: {aluno[2]}')
                print(f'mensalidade: {aluno[3]}')
            print(' - ')

# 5 funcionalidade
    elif op == 5:
        soma= 0
        contador = 0
        curso = input('Qual curso você deseja buscar a média?:')
        for aluno in alunos:
            if curso[2] == curso:
                soma += aluno[3]
                contador += 1
            media = soma / contador
            print(f'A média da mensalidade e{media}')

# 6 funcionalidade
    elif op == 6:
        mat = input('Digite a matricula do aluno:')
        for m in alunos:
            if mat == m[1]:
                atualiza = input('Qual dado você deseja: (N) (C) (M)').lower()
                if atualiza == 'n':
                    nome = input('Digite ')
                    alunos[0] = nome
                if atualiza == 'c':
                    nome = input('Digite ')
                    alunos[2] = curso
                if atualiza == 'm':
                    nome = input('Digite ')
                    alunos[3] = mat
                    print('Dados do aluno atualizados!')