import tkinter as tk
from tkinter import messagebox as mb

# configuración de widgets
# boton, label, input de texto
# colores '#00a8e8'
# Fuente Courier, 25



# Función para abrir la segunda ventana
def abrir_ventana_secundaria():
    # Ocultar ventana principal
    app.withdraw()

    # Crear segunda ventana
    juego = tk.Toplevel()
    juego.title("Juego")
    juego.geometry("300x200")
    juego.configure(background="#90d5fe")

    # Etiqueta en la segunda ventana
    etiqueta = tk.Label(juego, text="Estás en la ventana secundaria.")
    etiqueta.pack(pady=20)

    # Botón para volver a la ventana principal
    boton_volver = tk.Button(juego, text="Volver", command=lambda: volver(juego))
    boton_volver.pack(pady=10)

# Función para regresar a la ventana principal
def volver(juego):
    # Cierra la ventana secundaria
    juego.destroy()
    # Muestra la ventana principal
    app.deiconify()

# Configuración de la ventana principal

app = tk.Tk()
app.geometry("300x300")
app.configure(background="#90d5fe")
app.title("Piedra, papel, tijeras, lagarto, Spock")

# Botón para abrir la segunda ventana
boton_abrir = tk.Button(app, text="Abrir Ventana Secundaria", command=abrir_ventana_secundaria)
boton_abrir.pack(pady=20)


"""
palabra = tk.StringVar(app)
entrada = tk.StringVar(app)

app.geometry("300x300")
app.configure(background="#90d5fe")
app.title("Juego de la muerte")
#tk.Wm.wm_title(app, "Juego de la muerte") otra forma de ponerle el nombre a la aplicacion

def saludar():
    #mb.showinfo("Saludos", entrada.get())
    mb.showinfo("Viaja pronto","El juego de la muerte te espera")

def cambiarPalabra():
    palabra.set("Ocupado estoy durmiendo,  " + entrada.get())


tk.Button(
    app,
    text="Cambiar la palabra",
    font=("Courier", 14),
    bg="#f9ffa7",
    fg="black",
    command=cambiarPalabra

).pack(
    fill = tk.BOTH,
    expand = True
)

tk.Label(
    app,
    text="Mis muertos",
    fg="black",
    bg="#d7cdff",
    font=("Courier", 14),
    justify="center",
    textvariable=palabra
).pack(
    fill = tk.BOTH,
    expand = True
)

tk.Entry(
    fg="black",
    bg="#90d5fe",
    justify="center",
    font=("Courier", 14),
    textvariable=entrada
).pack(
    fill = tk.BOTH,
    expand = True
)
"""

app.mainloop()