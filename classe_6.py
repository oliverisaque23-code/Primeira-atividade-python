class Jogo:
    def __init__(self, nome, genero):
        self.nome = nome
        self.genero = genero

    def iniciar(self):
        print(f"Iniciando o jogo '{self.nome}' do gênero {self.genero}.")

    def desligar(self):
        print(f"Desligando o jogo '{self.nome}' do gênero {self.genero}.")

fifa = Jogo("Fifa", "Futebol/Esportes")
fifa.iniciar()
fifa.desligar()
