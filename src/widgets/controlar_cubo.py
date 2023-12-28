import tkinter as tk
from tkinter import messagebox

from modelos.movimiento import Movimiento
from constantes import colores

PADDING = 10

historial: list[str] = []

def crear_frame_control(raiz: tk.Misc, realizar_alg):
    """
    Crea y retorna el frame de control para la ventana del cubo.
    :param realizar_mov - debe ser una función que ejecute un movimiento y
        actualice el frame apropiadamente
    :param realizar_alg - muy parecido, la única diferencia es que debe
        ejecutar un algorithmo en vez de un movimiento
    """
    frame = tk.Frame(raiz, bg=colores.VERDE_2)

    def hacer_alg():
        texto = text_entrada.get().upper()
        alg = texto.split(' ')
        try:
            realizar_alg(alg)
            text_entrada.delete(0, tk.END)
            historial.extend(alg)
            text_historial.insert(tk.END, f' {texto}')
        except (ValueError, KeyError):
            messagebox.showerror('Error', 'Invalid Move Sequence Entered')

    text_historial = _crear_text_historial(frame)
    text_entrada = _crear_text_entrada(frame)
    frame_buttons = _crear_frame_buttons(frame, hacer_alg)

    text_historial.pack()
    text_entrada.pack()
    frame_buttons.pack()

    return frame


def _crear_text_historial(raiz: tk.Misc):
    return tk.Text(raiz, width=30, height=10)


def _crear_text_entrada(raiz: tk.Misc):
    return tk.Entry(raiz, width=30)


def _crear_frame_buttons(raiz: tk.Misc, hacer_alg):
    """
    Crea y retorna un frame de buttons para controlar el cubo
    """
    frame = tk.Frame(raiz, padx=PADDING, pady=PADDING)

    # crear botones
    button_aplicar = tk.Button(frame, text='Apply Algorithm', command=hacer_alg)
    button_deshacer = tk.Button(frame, text='Undo last move')

    button_invertir = tk.Button(frame, text='Invert Algorithm')
    button_reflejar = tk.Button(frame, text='Mirror Algorithm')

    button_png = tk.Button(frame, text='Export PNG')
    button_reset = tk.Button(frame, text='Reset Cube State')

    # posicionarlos
    button_aplicar.grid(row=0, column=0)
    button_deshacer.grid(row=0, column=1)

    button_invertir.grid(row=1, column=0)
    button_reflejar.grid(row=1, column=1)

    button_png.grid(row=2, column=0)
    button_reset.grid(row=2, column=1)

    return frame
