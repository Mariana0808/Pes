nota = [0, 0, 0, 0]
contador = 0
soma = 0

while contador < 4:
    nota[contador] = float(input(f"Digite a {contador + 1}ª nota: "))
    contador += 1

contador = 0

while contador < 4:
    soma = soma + nota[contador]
    contador += 1

media = soma / 4

print("Média:", media)

if media >= 6:
    print("Aprovado(a)")
else:
    print("Reprovado(a)")