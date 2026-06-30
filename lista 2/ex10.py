soma = 0
quantidade = 0

numero = int(input("Digite um número (0 para parar): "))

while numero != 0:
    soma += numero
    quantidade += 1

    numero = int(input("Digite um número (0 para parar): "))

if quantidade > 0:
    media = soma / quantidade
    print(f"Quantidade de números digitados: {quantidade}")
    print(f"Soma: {soma}")
    print(f"Média: {media:.2f}")
else:
    print("Nenhum número foi digitado.")