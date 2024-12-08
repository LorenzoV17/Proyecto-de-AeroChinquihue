import tkinter as tk
from tkinter import ttk, messagebox
from models.cliente import Cliente
from controllers.controlador_encomiendas import ControladorEncomiendas

class GUIEncomiendas:
    def __init__(self, master, vuelos):
        self.master = master
        self.vuelos = vuelos
        self.controlador = ControladorEncomiendas()
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

        tk.Label(self.master, text="Peso (kg)").grid(row=3, column=0)
        self.peso = tk.Entry(self.master)
        self.peso.grid(row=3, column=1)

        tk.Button(self.master, text="Enviar Encomienda", command=self.enviar_encomienda).grid(row=4, column=0, columnspan=2)

    def enviar_encomienda(self):
        cliente = Cliente(self.nombre.get(), self.rut.get())
        destino = self.destino.get()
        peso = float(self.peso.get())
        vuelo = next((v for v in self.vuelos if v.destino == destino), None)
        if vuelo:
            encomienda = self.controlador.crear_encomienda(cliente, peso, destino, vuelo)
            if encomienda:
                messagebox.showinfo("Éxito", f"Encomienda registrada: {encomienda}")
            else:
                messagebox.showerror("Error", "Peso excede la capacidad del avión")
