class carro:
    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor

    def pintar(self, nova_cor):
        self.cor = nova_cor

    def mostrar_cor(self):
        return self.cor


corro_ignacio = carro("gol", "preto")
carro_waltrick = carro("lamburguine", "vermelha")

corro_ignacio.pintar("azul")
carro_waltrick.pintar("verde")

print(corro_ignacio.mostrar_cor())
print(carro_waltrick.mostrar_cor())
