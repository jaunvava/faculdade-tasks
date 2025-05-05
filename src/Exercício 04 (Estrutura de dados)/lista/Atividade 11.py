# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média
# de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.


medias = []

for alunos in range(10):
    soma = 0
    for notas in range(4):
        nota = float(input("digite sua nota:"))
        soma = soma + nota
    media = soma / 4
    medias.append(media)

alunoAprov = 0
for media in medias:
    if media >= 7:
        alunoAprov += 1

print(f'a quantidade de aprovados foi: {alunoAprov}')
