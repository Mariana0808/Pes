divida = 1000
juros = 0.15  # 15% ao mês

meses = int(input("Digite a quantidade de meses: "))

contador = 0

while contador < meses:
    divida = divida + (divida * juros)
    contador += 1

print(f"Dívida após {meses} meses: R$ {divida:.2f}")