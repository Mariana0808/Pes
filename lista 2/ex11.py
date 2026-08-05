total_caixa = 0

while True:
    print("\n--- Cantina ---")
    print("1 - Suco (R$ 6,00)")
    print("2 - Pão de queijo (R$ 3,00)")
    print("3 - Pastel (R$ 7,00)")
    print("4 - Salada de frutas (R$ 9,00)")
    print("5 - Café com leite (R$ 3,50)")
    print("6 - Cappuccino (R$ 4,50)")
    print("7 - Iogurte (R$ 6,50)")
    print("8 - Água (R$ 2,50)")
    print("0 - Encerrar")

    codigo = int(input("Digite o código do produto: "))

    if codigo == 0:
        break

    quantidade = int(input("Digite a quantidade: "))

    if codigo == 1:
        nome = "Suco"
        preco = 6.00
    elif codigo == 2:
        nome = "Pão de queijo"
        preco = 3.00
    elif codigo == 3:
        nome = "Pastel"
        preco = 7.00
    elif codigo == 4:
        nome = "Salada de frutas"
        preco = 9.00
    elif codigo == 5:
        nome = "Café com leite"
        preco = 3.50
    elif codigo == 6:
        nome = "Cappuccino"
        preco = 4.50
    elif codigo == 7:
        nome = "Iogurte"
        preco = 6.50
    elif codigo == 8:
        nome = "Água"
        preco = 2.50
    else:
        print("Código inválido!")
        continue

    total_compra = preco * quantidade
    total_caixa += total_compra

    print(f"Produto: {nome}")
    print(f"Total da compra: R$ {total_compra:.2f}")

print(f"\nValor total acumulado no caixa: R$ {total_caixa:.2f}")