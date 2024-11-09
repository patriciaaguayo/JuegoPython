import random
import tkinter as tk
from tkinter import messagebox as mb
import cv2

# configuración de widgets
# boton, label, input de texto
# colores '#00a8e8'
# Fuente Courier, 25



# Opciones del juego

opciones = ["Piedra", "Papel", "Tijeras", "Lagarto", "Spock"]

# Reglas del juego

reglas = {
    "Tijeras": ["Papel", "Lagarto"], # Tijera gana contra papel y lagarto
    "Papel": ["Piedra", "Spock"], # Papel gana contra piedra y Spock
    "Piedra": ["Lagarto", "Tijeras"], # Piedra gana contra lagarto y tijeras
    "Lagarto": ["Spock", "Papel"], # Lagarto gana contra Spock y papel
    "Spock": ["Tijeras", "Piedra"] # Spock gana contra tijeras y piedra
}

"""
# Función que determina el ganador
def determinar_ganador(usuario, maquina):
    if usuario == maquina:
        return "Empate"
    elif maquina in reglas[usuario]:
        return "Usuario"
    else:
        return "Máquina"

# Función de manejo del juego al seleccionar una opción
def jugar(usuario):
    maquina = random.choice(opciones)
    ganador = determinar_ganador(usuario, maquina)

    resultado = f"Usuario eligió: {usuario}\nMáquina eligió: {maquina}\n\n"
    if ganador == "Empate":
        resultado += "Es un empate!"
    elif ganador == "Usuario":
        resultado += f"¡Usuario gana! {usuario} gana contra {maquina}."
    else:
        resultado += f"¡Máquina gana! {maquina} gana contra {usuario}."

    mb.showinfo("Resultado", resultado)
    
    """

# Función para abrir la segunda ventana
def abrir_ventana_juego():
    # Ocultar ventana principal
    app.withdraw()

    # Crear segunda ventana

    juego = tk.Toplevel()
    juego.title("Juego")
    juego.geometry("800x600")
    juego.configure(background="#90d5fe")

    # Contador de puntos

    etiqueta = tk.Label(
        juego,
        text="Partidas",
        font=("Courier", 14),
    )

    etiqueta.place(x=650, y=400)

    # Botón para volver a la ventana principal

    Volver = tk.Button(
        juego,
        text="Volver Principal",
        font=("Courier", 16),
        padx=10,
        pady=10,
        command=lambda: volver(juego))

    Volver.place(
        relx = 0.02,
        rely = 0.02,
        anchor = "nw"
    )

    # logica del juego

    x_pos = 0.1

    # Etiqueta de instrucciones
    Opciones = tk.Label(
        juego,
        text="SELECCIONA TU OPCIÓN:",
        font=("Courier", 16),
        bg="#90d5fe",
        pady=5,
        padx=5
    )

    Opciones.place(
        relx = 0.5,
        rely = 0.2,
        anchor = "center"
    )

    # Botones para cada opcion

    for opcion in opciones:
        button = tk.Button(
            juego,
            text=opcion,
            width=8,
            font=("Courier", 14),
            padx=8,
            pady=8,
            command=lambda o=opcion: jugar(o))

        button.place(
            relx=x_pos,  # Relación con el borde izquierdo
            rely=0.3,  # Relación con el borde superior
            anchor=tk.N  # Posición en la parte superior
        )
        x_pos += 0.2  # Incrementa la posición x para el próximo

    Resultado = tk.Label(
        juego,
        text="Resultado de la partida: ",
        font=("Courier", 16),
        bg="#90d5fe",
        pady=5,
        padx=5
    )

    Resultado.place(
        relx = 0.5,
        rely = 0.45,
        anchor = "center"
    )




# Función para regresar a la ventana principal

def volver(juego):
    # Cierra la ventana secundaria
    juego.destroy()
    # Muestra la ventana principal
    app.deiconify()

# Configuración de la ventana principal

app = tk.Tk()
app.geometry("800x600")
app.configure(background="#90d5fe")
app.title("Piedra, papel, tijeras, lagarto, Spock")

Titulo = tk.Label(
    app,
    text="Piedra, papel, tijeras, lagarto, Spock",
    font=("Courier", 24),
    bg="#90d5fe"
)

Titulo.place(
    relx = 0.5,
    rely = 0.1,
    anchor = "center"
)

# Botón para abrir la ventana de jugar

Jugar = tk.Button(
    app,
    text="Jugar",
    font=("Courier", 24),
    padx=20,
    pady=20,
    command=abrir_ventana_juego
)

Jugar.place(
           relx = 0.5,
           rely = 0.7,
           anchor = "center"
)


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