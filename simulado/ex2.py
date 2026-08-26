numero = []
contador = 0

while contador < 15:
    numero = int(input("digite um numero entre 1 e 75 "))
    if numero >= 1 and numero <=75:
        if numero not in numero :
            numero.append(numero)
            contador += 1
        else:
            print (numero repetido)
        else:
            print(numero invalido)
        

bingo=[]
i= 15
while  i >= 0:

    numero = int(input("digite um numero:   "))
    if numero >= 1 and numero <= 75 and not numero in bingo:
        bingo.append(numero)
        i = i - 1
    bingo . sort ()

print(bingo)
