class Onibus:
    def __init__(self, marca, capacidade):
        self.marca = marca
        self.capacidade = capacidade
        self.andando = False

    def andar(self):
        andando = True
        print(f"O ônibus {self.marca}, está andando com {self.capacidade} passageiros.")

    def parar(self):
        andando = False
        print(f"O ônibus {self.marca}, parou e está com {self.capacidade} passageiros.")

wolks = Onibus("Wolksvagen", 26)
wolks.andar()
wolks.parar()
