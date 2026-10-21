class CPU:
    def __init__(self, fabricante, modelo):
        self.fabricante = fabricante
        self.modelo = modelo


class Computador:
    def __init__(self, tipo, fabricante, modelo):
        self.tipo = tipo
        self.cpu = CPU(fabricante, modelo)


computador = Computador("Desktop", "Intel", "i7-12700K")

print("Tipo:", computador.tipo)
print("Fabricante da CPU:", computador.cpu.fabricante)
print("Modelo da CPU:", computador.cpu.modelo)

