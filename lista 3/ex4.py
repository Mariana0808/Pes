placas = ["-1"] * 15
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
        placa = input("Digite a placa do carro: ")

        indice = 0

        while indice < 15 and placas[indice] != "-1":
            indice += 1

        if indice < 15:
            placas[indice] = placa
            print("Placa cadastrada com sucesso!")
        else:
            print("Não há espaço disponível.")

    elif opcao == 2:
        placa = input("Digite a placa que deseja excluir: ")

        indice = 0

        while indice < 15 and placas[indice] != placa:
            indice += 1

        if indice < 15:
            placas[indice] = "-1"
            print("Placa excluída com sucesso!")
        else:
            print("Placa não encontrada.")

    elif opcao == 3:
        print("Placas cadastradas:")

        indice = 0

        while indice < 15:
            if placas[indice] != "-1":
                print(placas[indice])

            indice += 1

    elif opcao == 0:
        print("Programa encerrado!")

    else:
        print("Opção inválida!")