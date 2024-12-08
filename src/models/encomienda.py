class Encomienda:
    def __init__(self, cliente, peso, destino, precio_base):
        self.cliente = cliente
        self.peso = peso
        self.destino = destino
        self.precio = self.calcular_precio(precio_base)

    def calcular_precio(self, precio_base):
        descuento = self.cliente.obtener_descuento()
        return precio_base * self.peso * (1 - descuento)

    def __str__(self):
        return f"Encomienda de {self.peso} kg a {self.destino} - Precio: {self.precio} CLP"
