import tkinter as tk
from views.gui_reservas import GUIReservas
from views.gui_encomiendas import GUIEncomiendas
from views.gui_vuelos import GUIVuelos
from models.avion import Avion

class GUIMain:
    def __init__(self, master):
        self.master = master
        self.master.title("AeroChinquihue")
        self.aviones = [
            Avion("Cessna 310", 5, 910),
            Avion("Cessna 208 Caravan", 9, 1315),
            Avion("LET 410 UVP-E20", 19, 1800),
        ]
        self.vuelos = []  #Se cargan los vuelos generados
        self.setup_ui()

    def setup_ui(self):
        tk.Button(self.master, text="Gestión de Reservas", command=self.abrir_reservas).pack()
        tk.Button(self.master, text="Gestión de Encomiendas", command=self.abrir_encomiendas).pack()
        tk.Button(self.master, text="Gestión de Vuelos", command=self.abrir_vuelos).pack()

    def abrir_reservas(self):
        ventana = tk.Toplevel(self.master)
        GUIReservas(ventana, self.vuelos)

    def abrir_encomiendas(self):
        ventana = tk.Toplevel(self.master)
        GUIEncomiendas(ventana, self.vuelos)

    def abrir_vuelos(self):
        ventana = tk.Toplevel(self.master)
        GUIVuelos(ventana, self.aviones)
