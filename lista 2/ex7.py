quantidade_notas = int(input("Quantidade de notas: "))

soma = 0
contador = 0

while contador < quantidade_notas:
    nota = float(input(f"Digite a nota {contador + 1}: "))
    soma += nota
    contador += 1

media = soma / quantidade_notas

print(f"Média: {media:.2f}")

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")