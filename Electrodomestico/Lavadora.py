class Lavadora:
    def __init__(self, marca, modelo, capacidade_bateria, carga_atual, velocidade_motor):
        self.marca = marca
        self.modelo = modelo
        self.capacidade_bateria = capacidade_bateria
        self.carga_atual = carga_atual
        self.velocidade_motor = velocidade_motor
        self.ligada = False