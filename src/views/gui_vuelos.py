import tkinter as tk
from tkinter import ttk, messagebox
from controllers.controlador_vuelos import ControladorVuelos
from models.avion import Avion

class GUIVuelos:
    def __init__(self, master, aviones):
        self.master = master
        self.aviones = aviones
        self.controlador = ControladorVuelos(aviones)
        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.master, text="Destino").grid(row=0, column=0)
        self.destino = tk.Entry(self.master)
        self.destino.grid(row=0, column=1)

        tk.Label(self.master, text="Avión").grid(row=1, column=0)
        self.avion = ttk.Combobox(self.master, values=[avion.modelo for avion in self.aviones])
        self.avion.grid(row=1, column=1)

        tk.Button(self.master, text="Agregar Vuelo", command=self.agregar_vuelo).grid(row=2, column=0, columnspan=2)

    def agregar_vuelo(self):
        destino = self.destino.get()
        avion_modelo = self.avion.get()
        avion = next((a for a in self.aviones if a.modelo == avion_modelo), None)
        if avion:
            vuelo = self.controlador.crear_vuelo(destino, avion)
            if vuelo:
                messagebox.showinfo("Éxito", f"Vuelo creado: {vuelo}")
            else:
                messagebox.showerror("Error", "Destino no válido o avión no disponible")
