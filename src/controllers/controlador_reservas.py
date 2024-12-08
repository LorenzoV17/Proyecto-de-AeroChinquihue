from models.reserva import Reserva

class ControladorReservas:
    def __init__(self):
        self.reservas = []

    def crear_reserva(self, cliente, asiento, vuelo):
        if vuelo.seleccionar_asiento(asiento):
            reserva = Reserva(cliente, asiento, vuelo)
            self.reservas.append(reserva)
            return reserva
        return None

    def listar_reservas(self):
        return self.reservas
