# Pede para o usuário digitar um número
numero = int(input("Digite um número: "))

# A contagem sempre começa em 1
contador = 1

# Verifica se o número digitado é positivo ou igual a 1
if numero >= 1:

    # Enquanto o contador for menor ou igual ao número digitado
    while contador <= numero:

        # Mostra o valor atual do contador
        print(contador)

        # Soma 1 ao contador para passar para o próximo número
        contador = contador + 1

# Se o número for menor que 1 (negativo ou zero)
else:

    # Enquanto o contador for maior ou igual ao número digitado
    while contador >= numero:

        # Mostra o valor atual do contador
        print(contador)

        # Subtrai 1 do contador para ir descendo
        contador = contador - 1