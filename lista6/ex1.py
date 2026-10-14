# class Estudante:
#     nome = ""

# print("aaa")
# estudante1 = Estudante()
# estudante1.nome = "ignacio"
# print(estudante1.nome)

#class Estudante:
    #nota1=0
    #nota2=0
    #nota3=0
    #def __init__(self, nome, idade):
        #self.nome = nome
        #self.idade = idade
    
    #def conta(self):
        #return (self.nota1 + self.nota1 + self.nota1)/3

#print("aaa")
#estudante1 = Estudante("mariana", 17)
#print(estudante1.nome)
#print(estudante1.conta())

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def descricao(self):
        return f"{self.titulo} foi escrito por {self.autor}."


livro1 = Livro("Senhor dos Anéis", "Tolkien")
livro2 = Livro("Harry Potter", "J. K. Rowling")

print(livro1.descricao())
print(livro2.descricao())
