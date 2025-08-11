class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def ler(self):
        print(f"Lendo o livro '{self.titulo}' de {self.autor}.")

kaio = Livro("Senhor dos Anéis", "Desconhecido")
kaio.ler()
