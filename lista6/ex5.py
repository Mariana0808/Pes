
class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

    def exibir(self):
        return f"Meu nome é: {self.nome}, eu tenho: {self.idade} anos, eu meço: {self.altura} m e peso: {self.peso} kg"

    def IMC(self):
        imc = self.peso / (self.altura ** 2)
        self.imc = imc
        return imc

    def IMC_nome(self):
        return f"O meu nome é {self.nome} e o meu IMC é: {self.imc:.2f}"


ignacio = Pessoa("ignacio sepulveda", 25, 1.85, 98)
ryan = Pessoa("ryan", 25, 1.80, 90)
heloisa = Pessoa("heloisa", 17, 1.70, 59)

print(ignacio.exibir())
ignacio.IMC()
print(ignacio.IMC_nome())

print(ryan.exibir())
ryan.IMC()
print(ryan.IMC_nome())

print(heloisa.exibir())
heloisa.IMC()
print(heloisa.IMC_nome())
