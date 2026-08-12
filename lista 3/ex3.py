codigo = [-1] * 10
opcao = 0

while opcao != 3:
    print("\n===== MENU =====")
    print("1 - Cadastrar novo código")
    print("2 - Listar códigos cadastrados")
    print("3 - Sair")

    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        novo_codigo = int(input("Digite o código do produto: "))

        if novo_codigo == -1:
            print("Falha! O código -1 não pode ser cadastrado.")
        else:
            indice = 0

            while indice < 10 and codigo[indice] != -1:
                indice += 1

            if indice < 10:
                codigo[indice] = novo_codigo
                print("Código cadastrado com sucesso!")
            else:
                print("Falha! Não há espaço para cadastrar um novo código.")

    elif opcao == 2:
        print("\nCódigos cadastrados:")

        indice = 0

        while indice < 10:
            if codigo[indice] != -1:
                print(codigo[indice])

            indice += 1

    elif opcao == 3:
        print("Programa encerrado!")

    else:
        print("Opção inválida!")