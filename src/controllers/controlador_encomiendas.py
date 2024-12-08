from models.encomienda import Encomienda

class ControladorEncomiendas:
    def __init__(self):
        self.encomiendas = []

    def crear_encomienda(self, cliente, peso, destino, vuelo):
        if vuelo.avion.capacidad_carga >= peso:
            precio_base = vuelo.precio_encomienda
            encomienda = Encomienda(cliente, peso, destino, precio_base)
            vuelo.avion.capacidad_carga -= peso  #Se actualiza la carga
            self.encomiendas.append(encomienda)
            return encomienda
        return None

    def listar_encomiendas(self):
        return self.encomiendas

