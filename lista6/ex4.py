class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    def esta_disponivel(self):
        return self.quantidade > 0

    def vender(self):
        self.quantidade -= 1


produto = Produto("Arroz", 2)

print(produto.esta_disponivel())

produto.vender()
produto.vender()

print(produto.esta_disponivel())
