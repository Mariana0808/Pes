numero = int(input("Digite um número: "))

# Pede o início da tabuada
inicio = int(input("Digite o início da tabuada: "))

# Pede o fim da tabuada
fim = int(input("Digite o fim da tabuada: "))

# O contador começa no valor escolhido pelo usuário
contador = inicio

# Repete enquanto o contador for menor ou igual ao fim
while contador <= fim:

    # Mostra a multiplicação
    print(numero, "x", contador, "=", numero * contador)

    # Passa para o próximo valor
    contador = contador + 1