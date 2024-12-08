import tkinter as tk
from tkinter import messagebox


class Avion:
    def __init__(self, modelo, capacidad_pasajeros, capacidad_carga, precio_pasaje, precio_encomienda):
        self.modelo = modelo
        self.capacidad_pasajeros = capacidad_pasajeros
        self.capacidad_carga = capacidad_carga
        self.precio_pasaje = precio_pasaje
        self.precio_encomienda = precio_encomienda


class Cliente:
    def __init__(self, nombre, rut):
        self.nombre = nombre
        self.rut = rut


class Encomienda:
    def __init__(self, cliente, peso, destino, precio):
        self.cliente = cliente
        self.peso = peso
        self.destino = destino
        self.precio = precio


class ReservaVuelo:
    def __init__(self, cliente, avion, asiento, destino, precio):
        self.cliente = cliente
        self.avion = avion
        self.asiento = asiento
        self.destino = destino
        self.precio = precio


class AeroChinquihueApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AeroChinquihue - Sistema")

        #Se definen los aviones
        self.aviones = [
            Avion("Cessna 310", 5, 910, 20000, 5000),
            Avion("Cessna 208 Caravan", 9, 1315, 20000, 5000),
            Avion("LET 410 UVP-E20", 19, 1800, 30000, 8000)
        ]

        #Se definen los destinos y sus valores
        self.destinos = [
            ("Cochamo", 20000, 5000),
            ("Puelo Bajo", 20000, 5000),
            ("Contao", 20000, 5000),
            ("Rio Negro", 25000, 6000),
            ("Pupelde", 25000, 6000),
            ("Chepu", 30000, 8000),
            ("Ayacara", 30000, 8000),
            ("Pill´an", 40000, 12000),
            ("Reñihue", 40000, 12000),
            ("Isla Quenac", 40000, 12000),
            ("Palqui", 40000, 12000),
            ("Chaiten", 50000, 15000),
            ("Santa Barbara", 50000, 15000)
        ]

        #Se ingresan de vuelos y encomiendas
        self.reservas_vuelo = []
        self.registro_encomiendas = []

        #Se crea la interfaz grafica del proyecto
        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)

        #Botones de las opciones
        tk.Button(self.frame, text="Reservar Vuelo", command=self.reservar_vuelo).grid(row=0, column=0, padx=10, pady=10)
        tk.Button(self.frame, text="Ingresar Encomienda", command=self.registrar_encomienda).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(self.frame, text="Opciones del Gerente", command=self.menu_gerente).grid(row=2, column=0, padx=10, pady=10)

    def reservar_vuelo(self):
        reserva_window = tk.Toplevel(self.root)
        reserva_window.title("Reserva de Vuelo")

        #Datos del cliente
        tk.Label(reserva_window, text="Nombre del Cliente").grid(row=0, column=0)
        nombre_cliente = tk.Entry(reserva_window)
        nombre_cliente.grid(row=0, column=1)

        tk.Label(reserva_window, text="RUT del Cliente").grid(row=1, column=0)
        rut_cliente = tk.Entry(reserva_window)
        rut_cliente.grid(row=1, column=1)

        #Elección del destino
        tk.Label(reserva_window, text="Elije tu Destino").grid(row=2, column=0)
        destino_seleccionado = tk.StringVar(reserva_window)
        destino_seleccionado.set(self.destinos[0][0])
        destinos_menu = tk.OptionMenu(reserva_window, destino_seleccionado, *[destino[0] for destino in self.destinos])
        destinos_menu.grid(row=2, column=1)

        #Elección del avión
        tk.Label(reserva_window, text="Seleccionar Avión").grid(row=3, column=0)
        avion_seleccionado = tk.StringVar(reserva_window)
        avion_seleccionado.set(self.aviones[0].modelo)
        aviones_menu = tk.OptionMenu(reserva_window, avion_seleccionado, *[avion.modelo for avion in self.aviones])
        aviones_menu.grid(row=3, column=1)

        def actualizar_asientos(*args):
            modelo = avion_seleccionado.get()
            avion = next((a for a in self.aviones if a.modelo == modelo), None)
            if avion:
                asientos_menu["menu"].delete(0, "end")
                for i in range(1, avion.capacidad_pasajeros + 1):
                    asientos_menu["menu"].add_command(label=i, command=lambda value=i: asiento_seleccionado.set(value))
                asiento_seleccionado.set("1")

        avion_seleccionado.trace("w", actualizar_asientos)

        #Selección de asiento
        tk.Label(reserva_window, text="Seleccionar Asiento").grid(row=4, column=0)
        asiento_seleccionado = tk.StringVar(reserva_window)
        asiento_seleccionado.set("1")
        asientos_menu = tk.OptionMenu(reserva_window, asiento_seleccionado, "1")
        asientos_menu.grid(row=4, column=1)

        #Boton para confirmar reserva
        tk.Button(reserva_window, text="Confirma su Reserva", command=lambda: self.confirmar_reserva_vuelo(
            nombre_cliente.get(), rut_cliente.get(), destino_seleccionado.get(),
            avion_seleccionado.get(), asiento_seleccionado.get())).grid(row=5, columnspan=2, pady=10)

    def confirmar_reserva_vuelo(self, nombre, rut, destino, avion_modelo, asiento):
        avion = next((a for a in self.aviones if a.modelo == avion_modelo), None)
        destino_info = next((d for d in self.destinos if d[0] == destino), None)
        cliente = Cliente(nombre, rut)
        if avion and destino_info:
            precio = destino_info[1]
            reserva = ReservaVuelo(cliente, avion, asiento, destino, precio)
            self.reservas_vuelo.append(reserva)
            messagebox.showinfo("Reserva Confirmada", f"""
            Cliente: {cliente.nombre} (RUT: {cliente.rut})
            Destino: {destino}
            Avión: {avion.modelo}
            Asiento: {asiento}
            Precio: {precio} CLP
            """)

    def registrar_encomienda(self):
        encomienda_window = tk.Toplevel(self.root)
        encomienda_window.title("Registrar Encomienda")
        #Datos del cliente
        tk.Label(encomienda_window, text="Nombre del Cliente").grid(row=0, column=0)
        nombre_cliente = tk.Entry(encomienda_window)
        nombre_cliente.grid(row=0, column=1)

        tk.Label(encomienda_window, text="RUT del Cliente").grid(row=1, column=0)
        rut_cliente = tk.Entry(encomienda_window)
        rut_cliente.grid(row=1, column=1)

        #Elección de destino
        tk.Label(encomienda_window, text="Seleccionar Destino").grid(row=2, column=0)
        destino_seleccionado = tk.StringVar(encomienda_window)
        destino_seleccionado.set(self.destinos[0][0])
        destinos_menu = tk.OptionMenu(encomienda_window, destino_seleccionado, *[destino[0] for destino in self.destinos])
        destinos_menu.grid(row=2, column=1)

        #Peso de la encomienda
        tk.Label(encomienda_window, text="Peso de su Encomienda (kg)").grid(row=3, column=0)
        peso_encomienda = tk.Entry(encomienda_window)
        peso_encomienda.grid(row=3, column=1)

        #Boton para registrar encomienda
        tk.Button(encomienda_window, text="Registrar Encomienda", command=lambda: self.confirmar_encomienda(
            nombre_cliente.get(), rut_cliente.get(), destino_seleccionado.get(), peso_encomienda.get())).grid(row=4, columnspan=2, pady=10)

    def confirmar_encomienda(self, nombre, rut, destino, peso):
        try:
            peso = float(peso)
        except ValueError:
            messagebox.showerror("Error", "El peso debe ser un numero.")
            return

        destino_info = next((d for d in self.destinos if d[0] == destino), None)
        if destino_info:
            cliente = Cliente(nombre, rut)
            precio = destino_info[2] * peso
            encomienda = Encomienda(cliente, peso, destino, precio)
            self.registro_encomiendas.append(encomienda)
            messagebox.showinfo("Encomienda Registrada", f"""
            Cliente: {cliente.nombre} (RUT: {cliente.rut})
            Destino: {destino}
            Peso: {peso} kg
            Precio: {precio} CLP
            """)

    def menu_gerente(self):
        gerente_window = tk.Toplevel(self.root)
        gerente_window.title("Opciones del Gerente")

        #Se muestran los registros
        tk.Label(gerente_window, text="Registro de Vuelos").grid(row=0, column=0, sticky="w")
        vuelos_text = tk.Text(gerente_window, height=10, width=50)
        vuelos_text.grid(row=1, column=0, padx=10, pady=5)

        if self.reservas_vuelo:
            for reserva in self.reservas_vuelo:
                vuelos_text.insert("end", f"Cliente: {reserva.cliente.nombre}, Avión: {reserva.avion.modelo}, "
                                          f"Asiento: {reserva.asiento}, Destino: {reserva.destino}, "
                                          f"Precio: {reserva.precio} CLP\n")
        else:
            vuelos_text.insert("end", "No hay registros de vuelos.\n")

        tk.Label(gerente_window, text="Registro de Encomiendas").grid(row=2, column=0, sticky="w")
        encomiendas_text = tk.Text(gerente_window, height=10, width=50)
        encomiendas_text.grid(row=3, column=0, padx=10, pady=5)

        if self.registro_encomiendas:
            for encomienda in self.registro_encomiendas:
                encomiendas_text.insert("end", f"Cliente: {encomienda.cliente.nombre}, Peso: {encomienda.peso} kg, "
                                               f"Destino: {encomienda.destino}, Precio: {encomienda.precio} CLP\n")
        else:
            encomiendas_text.insert("end", "No hay registros de encomiendas.\n")

        #Se aplica el descuento
        tk.Label(gerente_window, text="Aplicar Descuento Especial").grid(row=4, column=0, sticky="w")
        tk.Label(gerente_window, text="Nombre Cliente").grid(row=5, column=0, sticky="w")
        cliente_descuento = tk.Entry(gerente_window)
        cliente_descuento.grid(row=5, column=1, padx=10, pady=5)

        tk.Label(gerente_window, text="Porcentaje Descuento (0-100%)").grid(row=6, column=0, sticky="w")
        descuento_porcentaje = tk.Entry(gerente_window)
        descuento_porcentaje.grid(row=6, column=1, padx=10, pady=5)

        tk.Button(gerente_window, text="Aplicar Descuento", command=lambda: self.aplicar_descuento(
            cliente_descuento.get(), descuento_porcentaje.get())).grid(row=7, columnspan=2, pady=10)

    def aplicar_descuento(self, cliente_nombre, porcentaje_descuento):
        try:
            porcentaje_descuento = float(porcentaje_descuento)
            if porcentaje_descuento < 0 or porcentaje_descuento > 100:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "El porcentaje debe estar entre 0 y 100.")
            return

        for reserva in self.reservas_vuelo:
            if reserva.cliente.nombre == cliente_nombre:
                descuento = reserva.precio * (porcentaje_descuento / 100)
                reserva.precio -= descuento
                messagebox.showinfo("Descuento Aplicado", f"Se aplicó un descuento del {porcentaje_descuento}%.\n"
                                                          f"Nuevo precio: {reserva.precio} CLP.")
                return

        messagebox.showerror("Error", f"No se encontró al cliente: {cliente_nombre}.")

#Se crea el proyecto
root = tk.Tk()
app = AeroChinquihueApp(root)
root.mainloop()
