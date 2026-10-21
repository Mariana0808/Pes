class Carro:
    def __init__(self, placa, modelo):
        self.placa = placa
        self.modelo = modelo


class VagaDeEstacionamento:
    def __init__(self, id_vaga):
        self.id_vaga = id_vaga
        self.carro_estacionado = None

    def ocupar_vaga(self, carro_obj):
        if self.carro_estacionado is None:
            self.carro_estacionado = carro_obj
            return True
        else:
            return False

    def liberar_vaga(self):
        self.carro_estacionado = None


# Programa principal
vaga = VagaDeEstacionamento("A-101")

carro1 = Carro("ABC-1234", "Honda Civic")
carro2 = Carro("XYZ-5678", "Toyota Corolla")

opcao = -1

while opcao != 0:
    print("\n--- MENU ---")
    print("1 - Verificar vaga")
    print("2 - Ocupar vaga")
    print("3 - Liberar vaga")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        if vaga.carro_estacionado is None:
            print("A vaga está livre.")
        else:
            print("Vaga ocupada!")
            print("Placa:", vaga.carro_estacionado.placa)
            print("Modelo:", vaga.carro_estacionado.modelo)

    elif opcao == 2:
        placa = input("Digite a placa do carro: ")
        modelo = input("Digite o modelo do carro: ")

        carro = Carro(placa, modelo)

        if vaga.ocupar_vaga(carro):
            print("Carro estacionado com sucesso!")
        else:
            print("A vaga já está ocupada!")

    elif opcao == 3:
        vaga.liberar_vaga()
        print("Vaga liberada!")

    elif opcao == 0:
        print("Programa encerrado.")

    else:
        print("Opção inválida!")
