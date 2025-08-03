class Transporte:
    def __init__(self, nome, capacidade):
        self.nome = nome
        self.capacidade = capacidade

    def mover(self):
        print(f"O transporte {self.nome} está se movendo.")

    def __str__(self):
        return f"{self.nome} (capacidade: {self.capacidade} pessoas)"


class Carro(Transporte):
    def __init__(self, nome, capacidade, combustivel):
        super().__init__(nome, capacidade)
        self.combustivel = combustivel

    def mover(self):
        print(f"O carro {self.nome} está dirigindo na estrada.")

    def abastecer(self):
        print(f"O carro {self.nome} está abastecendo com {self.combustivel}.")


class Bicicleta(Transporte):
    def __init__(self, nome, capacidade, tipo):
        super().__init__(nome, capacidade)
        self.tipo = tipo

    def mover(self):
        print(f"A bicicleta {self.nome} está pedalando na ciclovia.")

    def empinar(self):
        print(f"A bicicleta {self.nome} está empinando!")
