# Exemplo de uso de dicionário em Python
# Criando um dicionário com informações de um estudante
estudante = {
    "nome": "João Pedro",
    "idade": 21,
    "curso": "Ciência da Computação",
    "notas": [8.5, 9.0, 7.5],
}

# Acessando valores no dicionário
print("Nome:", estudante["nome"])
print("Idade:", estudante["idade"])
print("Curso:", estudante["curso"])
print("Notas:", estudante["notas"])

# Adicionando uma nova chave ao dicionário
estudante["cidade"] = "São Paulo"
print("\nApós adicionar a cidade:", estudante)

# Atualizando um valor existente
estudante["idade"] = 22
print("\nApós atualizar a idade:", estudante)

# Removendo uma chave do dicionário
del estudante["curso"]
print("\nApós remover o curso:", estudante)

# Iterando sobre o dicionário
print("\nIterando sobre o dicionário:")
for chave, valor in estudante.items():
    print(f"{chave}: {valor}")