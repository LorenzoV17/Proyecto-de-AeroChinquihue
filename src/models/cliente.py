class Cliente:
    def __init__(self, nombre, rut, vuelos_previos=0, emergencia=False):
        self.nombre = nombre #Datos del cliente
        self.rut = rut 
        self.vuelos_previos = vuelos_previos
        self.emergencia = emergencia

    def obtener_descuento(self):
        if self.emergencia:
            return 1.00  #Descuento de hasta 100%
        if self.vuelos_previos >= 10:
            return 0.10  #Descuento de 10%
        return 0.00

    def __str__(self):
        return f"{self.nombre} (RUT: {self.rut}) - {self.vuelos_previos} vuelos previos"
