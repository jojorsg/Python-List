class Carro:
    def __init__(self, placa, modelo):
        self.placa = placa
        self.modelo = modelo


class Estacionamento:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.vagas = []

    def estacionar_carro(self, carro):
        if len(self.vagas) < self.capacidade:
            self.vagas.append(carro)
            print("Carro estacionado com sucesso!")
        else:
            print("Estacionamento lotado!")

    def retirar_carro(self, placa):
        for carro in self.vagas:
            if carro.placa == placa:
                self.vagas.remove(carro)
                print("Carro retirado com sucesso!")
                return
        print("Carro não encontrado no estacionamento.")

    def listar_carros(self):
        if len(self.vagas) == 0:
            print("Estacionamento vazio!")
        else:
            for i, carro in enumerate(self.vagas):
                print(f"{i + 1}. Placa: {carro.placa}, Modelo: {carro.modelo}")



