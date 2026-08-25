amigos = []

opcao = 1

while opcao != 0:

    print("""
    1 - Cadastrar
    2 - Excluir
    3 - Listar
    0 - Sair
    """)

    print("Qual opção você quer?")

    opcao = int(input("R: "))

    if opcao == 1:

        amigo = input("Digite o amigo: ")

        amigos.append(amigo)

        print("Amigo cadastrado com sucesso!")

    elif opcao == 2:

        amigo = input("Digite o amigo que deseja excluir: ")

        if amigo in amigos:

            amigos.remove(amigo)

            print("Amigo excluído com sucesso!")

        else:

            print("Amigo não encontrado.")

    elif opcao == 3:

        if len(amigos) == 0:

            print("A lista de amigos está vazia.")

        else:

            print("Amigos cadastrados:")

            indice = 0

            while indice < len(amigos):

                print(amigos[indice])

                indice += 1

    elif opcao == 0:

        print("Programa encerrado!")

    else:

        print("Opção inválida!")