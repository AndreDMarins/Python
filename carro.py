from veiculo import Veiculo

class Carro(Veiculo):

    def __init__(self,cor, rodas, marca, tanque):
        Veiculo.__init__(self, cor,rodas,marca,tanque)

    def abastecer(self,litros):
        if self.tanque + litros > 50:
            print('Passou de 50 litros, abastecendo somente ' + str(50-self.tanque))
            self.tanque += (50-self.tanque)
        else:
            self.tanque += litros




