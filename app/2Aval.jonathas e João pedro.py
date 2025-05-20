usuarios = {'motoristas': [], 'passageiros': []}
caronas = []
reservas = []
usuario_logado = None
tipo_usuario_logado = None
print("          ===== Sistema de carona JJ =====")
while True:
    if usuario_logado == None:
        print(''' ---------------DIGITE-----------------
              
        1- Cadastrar MOTORISTA
        2- Cadastrar passageiro
        3- login
        0- Sair                
              
---------------------------------------''')
        opcao = input("Escolha uma opção: ")

        if opcao == "1":  
            nome = input("Nome completo: ")
            email = input("Email: ")
            senha = input("Senha: ")

            caracteres_proibidos = ['#', '!', '%', '&', '*']
            email_invalido = any(char in email for char in caracteres_proibidos)

            if email_invalido:
                print("Erro: Email contém caracteres inválidos do tipo:(#, !, %, &, *).")
            else:
                email_existe = any(u['email'] == email for u in usuarios['motoristas']) or \
                               any(u['email'] == email for u in usuarios['passageiros'])

                if email_existe:
                    print("Erro: Email já cadastrado.")
                elif not nome or not email or not senha:
                    print("Erro: Todos os campos são obrigatórios.")
                else:
                    usuarios['motoristas'].append({
                        "nome": nome,
                        "email": email,
                        "senha": senha,
                        "tipo": "motorista"
                    })
                    print("Motorista cadastrado com sucesso!")

        elif opcao == "2": 
            nome = input("Nome completo: ")
            email = input("Email: ")
            senha = input("Senha: ")

            caracteres_proibidos = ['#', '!', '%', '&', '*']
            email_invalido = any(char in email for char in caracteres_proibidos)

            if email_invalido:
                print("Erro: Email contém caracteres inválidos do tipo:(#, !, %, &, *).")
            else:
                email_existe = any(u['email'] == email for u in usuarios['motoristas']) or \
                               any(u['email'] == email for u in usuarios['passageiros'])

                if email_existe:
                    print("Erro: Email já cadastrado.")
                elif not nome or not email or not senha:
                    print("Erro: Todos os campos são obrigatórios.")
                else:
                    usuarios['passageiros'].append({
                        "nome": nome,
                        "email": email,
                        "senha": senha,
                        "tipo": "passageiro"
                    })
                    print("Passageiro cadastrado com sucesso!")

        elif opcao == "3": 
            print("\n===== Login =====")
            email = input("Email: ").strip().lower()
            senha = input("Senha: ").strip()

            caracteres_proibidos = ['#', '!', '%', '&', '*']
            email_invalido = any(char in email for char in caracteres_proibidos)

            if email_invalido:
                print("Erro: Email contém caracteres inválidos do tipo:(#, !, %, &, *).")
            else:
                usuario_encontrado = None
                tipo_usuario = None

                for motorista in usuarios['motoristas']:
                    if motorista['email'] == email and motorista['senha'] == senha:
                        usuario_encontrado = motorista
                        tipo_usuario = 'motorista'
                        break

                if not usuario_encontrado:
                    for passageiro in usuarios['passageiros']:
                        if passageiro['email'] == email and passageiro['senha'] == senha:
                            usuario_encontrado = passageiro
                            tipo_usuario = 'passageiro'
                            break

                if usuario_encontrado:
                    usuario_logado = usuario_encontrado
                    tipo_usuario_logado = tipo_usuario
                    print(f"Login bem-sucedido! Bem-vindo, {usuario_logado['nome']} ({tipo_usuario_logado})!")
                else:
                    print("Erro: Email ou senha incorretos.")

        elif opcao == "0":
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida.")

    else:  
        print("\n===== MENU (Usuário: " + usuario_logado["nome"] + f" - {tipo_usuario_logado}) =====")

        print("1- Listar Todas as Caronas")
        print("2- Buscar Carona por Origem e Destino")
        print("3- Mostrar Detalhes de Carona")
        print("9- Logout")
        print("0- Sair do Sistema")

        if tipo_usuario_logado == "motorista":
            print('                   ')
            print("4- Cadastrar Carona")
            print("5- Remover Carona")
            print("6- Minhas Caronas")

        if tipo_usuario_logado == "passageiro":
            print('                   ')
            print("7- Reservar Vaga em Carona")
            print("8- Cancelar Reserva")
            print("10- Avaliar Motorista")
            print('                   ')

        opcao = input("Escolha uma opção: ")

        if opcao == "1":  
            for c in caronas:
                if c["vagas"] > 0:
                    motorista = next((u for u in usuarios['motoristas'] if u["email"] == c["motorista"]), None)
                    if motorista:
                        print("-----------------")
                        print("Motorista:", motorista["nome"])
                        print("Origem:", c["origem"])
                        print("Destino:", c["destino"])
                        print("Data:", c["data"])
                        print("Horário:", c["horario"])
                        print("Vagas disponíveis:", c["vagas"])
                        print("Valor por vaga: R$", c["valor"])
                        print("-----------------")

        elif opcao == "2":  
            origem = input("Origem: ")
            destino = input("Destino: ")
            for c in caronas:
                if c["origem"].lower() == origem.lower() and c["destino"].lower() == destino.lower() and c["vagas"] > 0:
                    motorista = next((u for u in usuarios['motoristas'] if u["email"] == c["motorista"]), None)
                    if motorista:
                        print("-----------------")
                        print("Motorista:", motorista["nome"])
                        print("Data:", c["data"])
                        print("Horário:", c["horario"])
                        print("Valor: R$", c["valor"])
                        print("Vagas:", c["vagas"])
                        print("-----------------")

        elif opcao == "3":  
            email_motorista = input("Email do motorista: ")
            data = input("Data da carona: ")
            for c in caronas:
                if c["motorista"].lower() == email_motorista.lower() and c["data"] == data:
                    motorista = next((u for u in usuarios['motoristas'] if u["email"] == c["motorista"]), None)
                    if motorista:
                        print("Origem:", c["origem"])
                        print("Destino:", c["destino"])
                        print("Horário:", c["horario"])
                        print("Valor: R$", c["valor"])
                        print("Vagas restantes:", c["vagas"])
                        print("Passageiros:")
                        for p in c["passageiros"]:
                            passageiro = next((u for u in usuarios['passageiros'] if u["email"] == p), None)
                            if passageiro:
                                print(" -", passageiro["nome"])
                    break
            else:
                print("Carona não encontrada.")

        elif opcao == "4" and tipo_usuario_logado == "motorista":  
            origem = input("Origem: ")
            destino = input("Destino: ")
            data = input("Data (DD/MM/AA): ")
            horario = input("Horario: ")
            vagas = int(input("Quantidade de vagas: "))
            valor = float(input("Valor por vaga: "))
            caronas.append({
                "motorista": usuario_logado["email"],
                "origem": origem,
                "destino": destino,
                "data": data,
                "horario": horario,
                "vagas": vagas,
                "valor": valor,
                "passageiros": [],
                "avaliacoes": []
            })
            print("Carona cadastrada com sucesso.")

        elif opcao == "5" and tipo_usuario_logado == "motorista":
            data = input("Data da carona a remover (DD/MM/AA): ")
            quantidade_antes = len(caronas)

            caronas = [c for c in caronas if not (
                c["motorista"] == usuario_logado["email"] and 
                c["data"] == data
            )]
    
            if len(caronas) < quantidade_antes:
                print("Carona removida com sucesso.")
            else:
                print("Nenhuma carona encontrada para a data informada.")

        elif opcao == "6" and tipo_usuario_logado == "motorista": 
            minhas_caronas = [c for c in caronas if c["motorista"] == usuario_logado["email"]]
            if not minhas_caronas:
                print("Você não possui caronas cadastradas.")
            else:
                for c in minhas_caronas:
                    print("-----------------")
                    print("Origem:", c["origem"])
                    print("Destino:", c["destino"])
                    print("Data:", c["data"])
                    print("Horário:", c["horario"])
                    print("Valor: R$", c["valor"])
                    print("Vagas restantes:", c["vagas"])
                    print("Passageiros:")
                    for p in c["passageiros"]:
                        passageiro = next((u for u in usuarios['passageiros'] if u["email"] == p), None)
                        if passageiro:
                            print(" -", passageiro["nome"])
                    print("Avaliações:", c.get("avaliacoes", []))
                    print("-----------------")

        elif opcao == "7" and tipo_usuario_logado == "passageiro":  
            email_motorista = input("Email do motorista: ")
            data = input("Data da carona: ")
            for c in caronas:
                if c["motorista"].lower() == email_motorista.lower() and c["data"] == data:
                    if usuario_logado["email"] in c["passageiros"]:
                        print("Você já está nessa carona.")
                    elif c["vagas"] > 0:
                        c["vagas"] -= 1
                        c["passageiros"].append(usuario_logado["email"])
                        print("Reserva realizada com sucesso.")
                    else:
                        print("Erro: Não há vagas disponíveis.")
                    break
            else:
                print("Carona não encontrada.")

        elif opcao == "8" and tipo_usuario_logado == "passageiro":  
            email_motorista = input("Email do motorista: ")
            data = input("Data da carona: ")
            for c in caronas:
                if c["motorista"].lower() == email_motorista.lower() and c["data"] == data:
                    if usuario_logado["email"] in c["passageiros"]:
                        c["passageiros"].remove(usuario_logado["email"])
                        c["vagas"] += 1
                        print("Reserva cancelada.")
                    else:
                        print("Você não tem reserva nesta carona.")
                    break
            else:
                print("Carona não encontrada.")

        elif opcao == "10" and tipo_usuario_logado == "passageiro": 
            email_motorista = input("Email do motorista: ")
            data = input("Data da carona: ")
            for c in caronas:
                if c["motorista"].lower() == email_motorista.lower() and c["data"] == data:
                    if usuario_logado["email"] in c["passageiros"]:
                        nota = int(input("Informe uma nota de 1 a 5 para o motorista: "))
                        if 1 <= nota <= 5:
                            c.setdefault("avaliacoes", []).append(nota)
                            print("Avaliação registrada. Obrigado!")
                        else:
                            print("Nota inválida. Use um valor de 1 a 5.")
                    else:
                        print("Você não participou dessa carona.")
                    break
            else:
                print("Carona não encontrada.")

        elif opcao == "9":  
            usuario_logado = None
            tipo_usuario_logado = None
            print("Logout realizado.")

        elif opcao == "0": 
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida ou não permitida para seu tipo de usuário.")