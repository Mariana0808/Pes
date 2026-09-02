def distancia_total(quilometros,metros):
    total = (quilometros *1000) + metros 
    return total

quilometros = int(input("digite a quantidade de quilometros"))
metros = int (input("digite a quantidade de metros"))
distancia = distancia_total (quilometros,metros)

print("a distancia total percorrida foi:    ",distancia,"metros")