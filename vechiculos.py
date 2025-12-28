from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, color, marca, pasajeros, tipo_gasolina):
        self.color = color              # Un string [cite: 17, 18]
        self.marca = marca              # Un string [cite: 20, 21]
        self.pasajeros = pasajeros      # Un entero [cite: 23, 24]
        self.tipo_gasolina = tipo_gasolina # 'extra' o 'diesel' [cite: 26, 27]

    @abstractmethod
    def __str__(self):
        # El taller pide convertir este método en abstracto [cite: 37]
        pass

    @abstractmethod
    def conducir(self):
        # El error en el taller menciona que 'conducir' también es abstracto [cite: 41]
        pass


