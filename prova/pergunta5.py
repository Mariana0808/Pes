numero = int(input("digite um numero"))
i = 1

if numero >= 1:
    while i <= numero:
        print(i)
        i += 1
else:
    while i >= numero:
        print(i)
    i -=(i)

