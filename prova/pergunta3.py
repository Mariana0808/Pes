quantidade = int(input("quantas palavras deseja cadastrar?  "))

dicionario = {
   "amor" : "sentimento de carinho",
   "pena" : "sentimento de pena", 
   "mariana" : "menina burra",
}

for i in range (quantidade):
    palavra = input("digite a palavra:   ")
    signifiado = input("digite a signifiado:   ")
    dicionario[palavra] = signifiado 
print(dicionario)
