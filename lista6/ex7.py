class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

    def exibir(self):
        return f"Meu nome é: {self.nome}, tenho {self.idade} anos, meço {self.altura} m e peso {self.peso} kg."

    def IMC(self):
        imc = self.peso / (self.altura ** 2)
        self.imc = imc
        return imc

    def IMC_nome(self):
        return f"O meu nome é {self.nome} e o meu IMC é: {self.imc:.2f}"


pessoas = []

while True:
    print("\nCadastro de Pessoas")
    print("-------------------")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Excluir")
    print("4 - Atualizar")
    print("0 - Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        altura = float(input("Digite a altura: "))
        peso = float(input("Digite o peso: "))

        pessoa = Pessoa(nome, idade, altura, peso)
        pessoas.append(pessoa)

        print("Pessoa cadastrada com sucesso!")

    elif opcao == "2":
        if len(pessoas) == 0:
            print("Nenhuma pessoa cadastrada.")
        else:
            for pessoa in pessoas:
                print(pessoa.exibir())
                pessoa.IMC()
                print(pessoa.IMC_nome())
                print("-------------------")

    elif opcao == "3":
        nome = input("Digite o nome da pessoa que deseja excluir: ")

        encontrada = False

        for pessoa in pessoas:
            if pessoa.nome.lower() == nome.lower():
                pessoas.remove(pessoa)
                encontrada = True
                print("Pessoa excluída com sucesso!")
                break

        if not encontrada:
            print("Pessoa não encontrada.")

    elif opcao == "4":
        nome = input("Digite o nome da pessoa que deseja atualizar: ")

        encontrada = False

        for pessoa in pessoas:
            if pessoa.nome.lower() == nome.lower():
                pessoa.idade = int(input("Digite a nova idade: "))
                pessoa.altura = float(input("Digite a nova altura: "))
                pessoa.peso = float(input("Digite o novo peso: "))

                encontrada = True
                print("Dados atualizados com sucesso!")
                break

        if not encontrada:
            print("Pessoa não encontrada.")

    elif opcao == "0":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida! Tente novamente.")