idades = []
contador = 0

while contador < 6:
    idade = int(input(f"Digite a idade do {contador + 1}º aluno: "))
    idades.append(idade)
    contador += 1

contador = 0

print("Idades maiores ou iguais a 16:")

while contador < 6:
    if idades[contador] >= 16:
        print(idades[contador])
    contador += 1
