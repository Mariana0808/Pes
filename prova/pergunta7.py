placas = []
opcao = -1

while opcao !=0:
   
    print( """menu
    1- cadastrar
    2- excluir
    3-listar
    0-sair""")

    opcao = int (input("digite uma opcao:   "))

    if opcao == 1:
        placa = input("digite o nome da placa: ")
        placas.append(placa)
      
        print("cadrastro realizado com sucesso")
    elif opcao == 2:
        placa = input("digite a placa que deseja excluir:   ")
        if placa in placas:
            placas.remove(placa)
        
            print("placa excluido com sucesso")
        else:
            print("falha!")
    elif opcao == 3:
        i = 0
        while i <len(placas):
            print(placas[i])
            i += 1 
        
    elif opcao == 0:
        print("saindo...")
    else:
        print("opcao invalida")