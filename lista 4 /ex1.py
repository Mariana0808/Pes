bairros = ["Centro"]

contador = 0

while contador < 5:
    nome = input(f"Digite o nome do bairro {contador + 2}: ")
    bairros.append(nome)
    contador += 1

print("\nBairros cadastrados:")

for bairro in bairros:
    print(bairro)
