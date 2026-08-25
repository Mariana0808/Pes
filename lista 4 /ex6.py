notas = []

opcao = 1

while opcao != 0:

    print("""
    1 - Cadastrar
    2 - Excluir
    3 - Listar
    4 - Calcular média
    0 - Sair
    """)

    print("Qual opção você quer?")

    opcao = int(input("R: "))

    if opcao == 1:

        nota = float(input("Digite a nota: "))

        notas.append(nota)

        print("Nota cadastrada com sucesso!")

    elif opcao == 2:

        if len(notas) == 0:

            print("A lista de notas está vazia.")

        else:

            indice = int(input("Digite o índice da nota que deseja excluir: "))

            if indice >= 0 and indice < len(notas):

                notas.pop(indice)

                print("Nota excluída com sucesso!")

            else:

                print("Índice inválido.")

    elif opcao == 3:

        if len(notas) == 0:

            print("A lista de notas está vazia.")

        else:

            print("Notas cadastradas:")

            indice = 0

            while indice < len(notas):

                print(f"Índice {indice}: {notas[indice]}")

                indice += 1

    elif opcao == 4:

        if len(notas) == 0:

            print("Não é possível calcular a média. A lista está vazia.")

        else:

            soma = 0
            indice = 0

            while indice < len(notas):

                soma += notas[indice]

                indice += 1

            media = soma / len(notas)

            print(f"Média: {media:.2f}")

            if media >= 6:

                print("Aprovado!")

            else:

                print("Reprovado!")

    elif opcao == 0:

        print("Programa encerrado!")

    else:

        print("Opção inválida!")
