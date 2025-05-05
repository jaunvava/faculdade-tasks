
usuarios = []
usuarios_motorista = []
dados_usuario = {'nome':'', 'email':'', 'senha':''}
caronas_disponiveis = {}
caracter_invalido = ['#','!','$','%','&']

while True:
    print("\n====== Sistema de Caronas ======")
    print("1. Fazer Login")
    print("2. Cadastrar Usuário")
    print("3. Cadastrar Motorista")
    print("4. Sair do sistema")
    opcao = input("Escolha uma opção:")


    if opcao == '1':
        print("\n=== Fazer login ===")
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")


    elif opcao == "2":
        print("\n=== Cadastro de Usuário ===")
        nome = input("Digite seu nome completo:")
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
    
    # elif opcao == "3":
    #     print("\n=== Cadastrar Motorista ===")
    #     nome_motorista = input("Motorita digite seu nome completo: ")
    #     email_motorista = input("Motorita digite seu email: ")
    #     senha_motorista = input("Motorita digite sua senha: ")

    elif opcao == "4":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")

    if opcao == '3':
        for motorista in usuarios_motorista:
         if motorista["email"] == email_motorista:
            email_motor_existente = True
            break


        if email_existente:
            print("Erro: Este email já está cadastrado como motorista.")
        else:
            usuarios_motorista.append({"nome": nome_motorista, "email": email_motorista, "senha": senha_motorista})
            print("Cadastro de motorista realizado com sucesso!")
        
    elif opcao == "1":
        print("\n=== Fazer login ===")
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")

        usuario_logado = None
        for usuario in usuarios + usuarios_motorista:
            if usuario["email"] == email and usuario["senha"] == senha:
                usuario_logado = usuario
                break

        if usuario_logado:
            print(f"Bem-vindo(a), {usuario_logado['nome']}!")
            if usuario_logado in usuarios_motorista:
                print("\n=== Oferecer Carona ===")
                origem = input("Digite a origem da carona: ")
                destino = input("Digite o destino da carona: ")
                horario = input("Digite o horário da carona: ")

            if email not in caronas:
                caronas[email] = []

            caronas[email].append({"origem": origem, "destino": destino, "horario": horario})
            print("Carona oferecida com sucesso!")
        else:
            print("Erro: Email ou senha inválidos.")