preço = int(input("digite o preço"))
quantidadecomprada = int(input("digite a quantidade comprada"))

total = preço * quantidadecomprada

if total >= 100:
    print(total * 0.90)
else: 
    print(total)