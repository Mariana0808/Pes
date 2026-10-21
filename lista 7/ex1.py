class MarcadorDePagina:
    def __init__(self, pagina_atual):
        self.pagina_atual = pagina_atual


class Livro:
    def __init__(self, titulo, total_paginas):
        self.titulo = titulo
        self.total_paginas = total_paginas
        self.marcador = None

    def adicionar_marcador(self, pagina):
        if self.marcador is None:
            self.marcador = MarcadorDePagina(pagina)
        else:
            self.marcador.pagina_atual = pagina


livro = Livro("Harry Potter", 300)

livro.adicionar_marcador(30)
print(livro.marcador.pagina_atual)

livro.adicionar_marcador(50)
print(livro.marcador.pagina_atual)
