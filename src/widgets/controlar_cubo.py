import tkinter as tk

from modelos.cubo import Cubo
from modelos.movimiento import Movimiento
from constantes import colores
from constantes.enums import Cara

PADDING = 10

historial: list[Movimiento] = [Movimiento(Cara.B, 1, 1, False), Movimiento(Cara.B, 1, 1, False)]

def crear_frame_control(raiz: tk.Misc):
    frame = tk.Frame(raiz, bg=colores.VERDE_2)

    text_historial = _crear_frame_historial(frame)
    text_entrada = _crear_frame_entrada(frame)
    frame_buttons = _crear_frame_buttons(frame)

    text_historial.pack()
    text_entrada.pack()
    frame_buttons.pack()

    return frame


def _crear_frame_historial(raiz: tk.Misc):
    frame = tk.Frame(raiz, padx=PADDING, pady=PADDING)

    label = tk.Label(frame, text='Moves applied:')
    text = tk.Text(frame, width=30, height=10)
    text.insert(1.0, str(historial))
    text.configure(state="disabled")

    label.pack()
    text.pack()

    return frame


def _crear_frame_entrada(raiz: tk.Misc):
    frame = tk.Frame(raiz, padx=PADDING, pady=PADDING)

    label = tk.Label(frame, text='Sequence of moves:')
    text = tk.Entry(frame, width=30)

    label.pack()
    text.pack()

    return frame


def _crear_frame_buttons(raiz: tk.Misc):
    frame = tk.Frame(raiz, padx=PADDING, pady=PADDING)

    # crear botones
    button_aplicar = tk.Button(frame, text='Apply Algorithm')
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
