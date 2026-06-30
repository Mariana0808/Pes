deposito = float(input("Digite o valor depositado mensalmente: R$ "))

saldo = 0
mes = 1

while mes <= 24:
    saldo = saldo * 1.005  # rendimento de 0,5%
    saldo = saldo + deposito

    print(f"Mês {mes}: R$ {saldo:.2f}")

    mes += 1