import random
import tkinter as tk
from tkinter import messagebox as mb
import cv2

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

def reiniciar_puntos():
    ganados_jugador_var.set("0")
    ganados_maquina_var.set("0")
    empates_var.set("0")

def determinar_ganador(opcion_jugador, opcion_maquina):
    global ganados_jugador_var, ganados_maquina_var, empates_var

    if opcion_jugador == opcion_maquina:
        empates_var.set(str(int(empates_var.get()) + 1))
        return "Empate"
    elif opcion_maquina in reglas[opcion_jugador]:
        ganados_jugador_var.set(str(int(ganados_jugador_var.get()) + 1))
        return f"{opcion_jugador} gana a {opcion_maquina}. Gana jugador!!"
    else:
        ganados_maquina_var.set(str(int(ganados_maquina_var.get()) + 1))
        return f"{opcion_maquina} gana a {opcion_jugador}. Gana máquina!!"

def jugar(opcion_jugador):
    opcion_maquina = random.choice(opciones)
    resultado = determinar_ganador(opcion_jugador, opcion_maquina)
    resultado_var.set(f"(J) {opcion_jugador} vs (M) {opcion_maquina}. {resultado}")
    mb.showinfo("Resultado", f" (Jugador) {opcion_jugador} vs (Máquina) {opcion_maquina}. {resultado}")

# Función para abrir la segunda ventana
def abrir_ventana_juego():
    # Ocultar ventana principal
    app.withdraw()

    # Crear segunda ventana

    juego = tk.Toplevel()
    juego.title("Juego")
    juego.geometry("800x600")
    juego.configure(background="#90d5fe")

    global empates_var, ganados_jugador_var, ganados_maquina_var, resultado_var

    empates_var = tk.StringVar()
    empates_var.set("0")

    ganados_jugador_var = tk.StringVar()
    ganados_jugador_var.set("0")

    ganados_maquina_var = tk.StringVar()
    ganados_maquina_var.set("0")

    # Crear un StringVar para el Label Result
    resultado_var = tk.StringVar()
    resultado_var.set("")

    # Contador de puntos

    partidas_frame = tk.Frame(juego)
    partidas_frame.place(relx=0.5, rely=0.8, anchor="center")

    etiqueta = tk.Label(
        partidas_frame,
        text="PARTIDAS",
        font=("Courier", 14),
        width=30,
        pady=20,
        padx=20
    )
    etiqueta.pack(side="top")

    # Jugador
    jugador_frame = tk.Frame(partidas_frame)
    jugador_frame.pack(side="top", pady=10)

    jugador_label = tk.Label(
        jugador_frame,
        text="Jugador:",
        font=("Courier", 14),
    )
    jugador_label.pack(side="left")

    jugador_ganados_valor = tk.Label(
        jugador_frame,
        textvariable=ganados_jugador_var,
        font=("Courier", 14),
    )
    jugador_ganados_valor.pack(side="left", padx=10)

    # Máquina
    maquina_frame = tk.Frame(partidas_frame)
    maquina_frame.pack(side="top", pady=10)

    maquina_label = tk.Label(
        maquina_frame,
        text="Máquina:",
        font=("Courier", 14),
    )
    maquina_label.pack(side="left")

    maquina_ganadas_valor = tk.Label(
        maquina_frame,
        textvariable=ganados_maquina_var,
        font=("Courier", 14),
    )
    maquina_ganadas_valor.pack(side="left", padx=10)

    # Empates
    empates_frame = tk.Frame(partidas_frame)
    empates_frame.pack(side="top", pady=10)

    empates_label = tk.Label(
        empates_frame,
        text="Empates:",
        font=("Courier", 14),
        pady=5
    )
    empates_label.pack(side="left")

    empates_valor = tk.Label(
        empates_frame,
        textvariable=empates_var,
        font=("Courier", 14),
    )
    empates_valor.pack(side="left", padx=10)

    # Botón para reiniciar el juego

    Reiniciar = tk.Button(
        juego,
        text="Reiniciar",
        font=("Courier", 16),
        padx=10,
        pady=10,
        bg="#f9ffa7",
        command=lambda: reiniciar_puntos())

    Reiniciar.place(
        relx = 0.98,
        rely = 0.02,
        anchor = "ne"
    )

    Reiniciar.config(bg="green")

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

    Result = tk.Label(
        juego,
        font=("Courier", 16),
        bg="white",
        pady=5,
        padx=5,
        width=70,
        textvariable=resultado_var
    )

    Result.place(relx=0.5, rely=0.55, anchor="center")


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