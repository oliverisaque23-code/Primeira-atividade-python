class Computador:
    def __init__(self, marca):
        self.marca = marca
        self.ligado = False

    def ligar(self):
        self.ligado = True
        print(f"O computador {self.marca} está ligado.")

    def desligar(self):
        self.ligado = False
        print(f"O computador {self.marca} está desligado.")


fe16 = Computador("FE16")
fe16.ligar()
fe16.desligar()
