# Pede para o usuário digitar um número
numero = int(input("Digite um número: "))

# Cria a variável contador e começa a contagem em 0
contador = 0

# Enquanto o contador for menor ou igual ao número digitado
while contador <= numero:

    # Mostra o valor atual do contador na tela
    print(contador)

    # Soma 2 ao contador para ir para o próximo número par
    contador = contador + 2
