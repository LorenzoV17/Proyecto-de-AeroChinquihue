class Vuelo:
    def __init__(self, destino, precio_pasaje, precio_encomienda, avion):
        self.destino = destino
        self.precio_pasaje = precio_pasaje
        self.precio_encomienda = precio_encomienda
        self.avion = avion
        self.asientos_disponibles = list(range(1, avion.capacidad_pasajeros + 1))  #Se generan los asientos

    def seleccionar_asiento(self, asiento):
        if asiento in self.asientos_disponibles:
            self.asientos_disponibles.remove(asiento)
            return True
        return False

    def __str__(self):
        return f"Vuelo a {self.destino} - {self.avion.modelo} - {len(self.asientos_disponibles)} asientos disponibles"
