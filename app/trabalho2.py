'''O sistema deve ser capaz de cadastrar caronas, permitir reservas e exibir os dados 
no terminal'''

# Lista para armazenar os usuários cadastrados
usuarios = []
dados_usuario = {'nome':'joao', 'email': 'joaoteste@gmail.com', 'senha':123}
caronas = {}

while True:
    print("\n====== Sistema de Caronas ======")
    print("1. Fazer Login")
    print("2. Cadastrar Usuário")
    print("3. Cadastrar Motorista")
    print("4. Sair")
    opcao = input("Escolha uma opção:")

    if opcao == "1":
        print("\n=== Cadastro de Usuário ===")
        nome = input("Digite seu nome completo: ")
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")

        email_existente = False
        for usuario in usuarios:
            if usuario["email"] == email:
                email_existente = True
                break

        if email_existente:
            print("Erro: Este email já está cadastrado.")
        else:
            usuarios.append({"nome": nome, "email": email, "senha": senha})
            print("Cadastro realizado com sucesso!")

    elif opcao == "2":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")