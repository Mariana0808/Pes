nomes = ["-1"] * 15
idades = ["-1"] * 15
alturas = ["-1"] * 15
pesos = ["-1"] * 15

opcao = 1

while opcao != 0:
    print("""
    1 - Cadastrar
    2 - Excluir
    3 - Alterar
    4 - Listar
    0 - Sair
    """)

    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        posicao = -1

        for i in range(15):
            if nomes[i] == "-1":
                posicao = i
                break

        if posicao == -1:
            print("Não há espaço para cadastrar.")

        else:
            nomes[posicao] = input("Digite o nome: ")
            idades[posicao] = int(input("Digite a idade: "))
            alturas[posicao] = float(input("Digite a altura: "))
            pesos[posicao] = float(input("Digite o peso: "))

            print("Cadastro realizado com sucesso!")

    elif opcao == 2:
        nome = input("Digite o nome que deseja excluir: ")
        posicao = -1

        for i in range(15):
            if nomes[i] == nome:
                posicao = i
                break

        if posicao == -1:
            print("Pessoa não encontrada.")

        else:
            nomes[posicao] = "-1"
            idades[posicao] = "-1"
            alturas[posicao] = "-1"
            pesos[posicao] = "-1"

            print("Cadastro excluído!")

    elif opcao == 3:
        nome = input("Digite o nome que deseja alterar: ")
        posicao = -1

        for i in range(15):
            if nomes[i] == nome:
                posicao = i
                break

        if posicao == -1:
            print("Pessoa não encontrada.")

        else:
            idades[posicao] = int(input("Digite a nova idade: "))
            alturas[posicao] = float(input("Digite a nova altura: "))
            pesos[posicao] = float(input("Digite o novo peso: "))

            print("Cadastro alterado!")

    elif opcao == 4:
        for i in range(15):
            if nomes[i] != "-1":
                print("Nome:", nomes[i])
                print("Idade:", idades[i])
                print("Altura:", alturas[i])
                print("Peso:", pesos[i])
                print("--------------------")

    elif opcao == 0:
        print("Programa encerrado!")

    else:
        print("Opção inválida!")