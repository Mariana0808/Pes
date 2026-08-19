notas = []
contador = 0

quantidade = int(input("Quantas notas serão digitadas? "))

while contador < quantidade:
    nota = float(input(f"Digite a {contador + 1}ª nota: "))
    notas.append(nota)
    contador += 1
print("\nExibição com while:")

contador = 0

while contador < quantidade:
    print(f"{contador + 1}ª nota: {notas[contador]}")
    contador += 1
    
print("\nExibição com for:")

for nota in notas:
    print(f"Nota: {nota}")