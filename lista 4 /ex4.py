cidades = []
contador = 0

quantidade = int(input("Quantas  cidades que devem ser cadastradas?"))

while contador < quantidade:
    nome = input(f"Digite a {contador + 1}ª cidade: ")
    cidades.append(nome)
    contador += 1

contador = 0

while contador < quantidade:
    print(f"{contador + 1}ª cidades: {cidades[contador]}")
    contador += 1

cidade = input("Digite o nome da cidade que deseja remover: ")

cidades.remove(cidade)

print(cidades)
























bairros = ["Centro"]

contador = 0

while contador < 5:
    nome = input(f"Digite o nome do bairro {contador + 2}: ")
    bairros.append(nome)
    contador += 1

print("\nBairros cadastrados:")

for bairro in bairros:
    print(bairro)