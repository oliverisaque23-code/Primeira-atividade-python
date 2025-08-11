class Bicicleta:
    def __init__(self, cor, tipo):
        self.cor = cor
        self.tipo = tipo

    def pedalar(self):
        print(f"Pedalando a bicicleta {self.tipo} de cor {self.cor}.")

bike = Bicicleta("branca", "porte grande")
bike.pedalar()
