from models.vuelo import Vuelo

class ControladorVuelos:
    def __init__(self, aviones):
        self.vuelos = []
        self.aviones = aviones

    def crear_vuelo(self, destino, avion):
        precios = {
            "Puerto Montt": (20000, 5000),
            "Cochamó": (20000, 5000),
            "Pillán": (40000, 12000),
        }
        if destino in precios:
            precio_pasaje, precio_encomienda = precios[destino]
            vuelo = Vuelo(destino, precio_pasaje, precio_encomienda, avion)
            self.vuelos.append(vuelo)
            return vuelo
        return None
