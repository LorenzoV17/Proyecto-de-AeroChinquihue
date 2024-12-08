import tkinter as tk
from tkinter import ttk, messagebox
from models.cliente import Cliente
from controllers.controlador_reservas import ControladorReservas

class GUIReservas:
    def __init__(self, master, vuelos):
        self.master = master
        self.vuelos = vuelos
        self.controlador = ControladorReservas()
        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.master, text="Nombre").grid(row=0, column=0)
        self.nombre = tk.Entry(self.master)
        self.nombre.grid(row=0, column=1)

        tk.Label(self.master, text="RUT").grid(row=1, column=0)
        self.rut = tk.Entry(self.master)
        self.rut.grid(row=1, column=1)

        tk.Label(self.master, text="Destino").grid(row=2, column=0)
        self.destino = ttk.Combobox(self.master, values=[vuelo.destino for vuelo in self.vuelos])
        self.destino.grid(row=2, column=1)

        tk.Label(self.master, text="Asiento").grid(row=3, column=0)
        self.asiento = tk.Entry(self.master)
        self.asiento.grid(row=3, column=1)

        tk.Button(self.master, text="Reservar", command=self.reservar).grid(row=4, column=0, columnspan=2)

    def reservar(self):
        cliente = Cliente(self.nombre.get(), self.rut.get())
        destino = self.destino.get()
        vuelo = next((v for v in self.vuelos if v.destino == destino), None)
        if vuelo:
            asiento = int(self.asiento.get())
            reserva = self.controlador.crear_reserva(cliente, asiento, vuelo)
            if reserva:
                messagebox.showinfo("Éxito", f"Reserva exitosa: {reserva}")
            else:
                messagebox.showerror("Error", "Asiento no disponible")
