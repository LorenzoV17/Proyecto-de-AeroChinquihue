class Avion:
    def __init__(self, modelo, capacidad_pasajeros, capacidad_carga):
        self.modelo = modelo
        self.capacidad_pasajeros = capacidad_pasajeros
        self.capacidad_carga = capacidad_carga

    def __str__(self):
        return f"{self.modelo} - {self.capacidad_pasajeros} pasajeros, {self.capacidad_carga} kg de carga"
