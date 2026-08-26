ano = int(input("Digite o ano"))
if ano % 4 == 0 or ano % 400 ==0:
    print("é ano bissexto")
else:
    print(" não é ano bissexto")