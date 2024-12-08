class Reserva:
    def __init__(self, cliente, asiento, vuelo):
        self.cliente = cliente
        self.asiento = asiento
        self.vuelo = vuelo
        self.precio = self.calcular_precio()

    def calcular_precio(self):
        descuento = self.cliente.obtener_descuento()
        return self.vuelo.precio_pasaje * (1 - descuento)

    def __str__(self):
        return f"Reserva de {self.cliente.nombre} en asiento {self.asiento} para el vuelo a {self.vuelo.destino} - Precio: {self.precio} CLP"
