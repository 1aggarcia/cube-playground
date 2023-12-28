import tkinter as tk
from tkinter import messagebox

import modelos.movimiento as mv
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

    def deshacer():
        mov = mv.movimiento_de_texto(historial.pop())
        invertido = mv.invertir_movimiento(mov)
        realizar_alg([str(invertido)])
        text_historial.delete(1.0, tk.END)
        text_historial.insert(1.0, str(historial))

    text_historial = tk.Text(frame, width=30, height=10)
    text_entrada = tk.Entry(frame, width=30)
    frame_buttons = _crear_frame_buttons(frame, hacer_alg, deshacer)

    text_historial.pack()
    text_entrada.pack()
    frame_buttons.pack()

    return frame


def _crear_frame_buttons(raiz: tk.Misc, hacer_alg, deshacer):
    """
    Crea y retorna un frame de buttons para controlar el cubo
    """
    frame = tk.Frame(raiz, padx=PADDING, pady=PADDING)

    # crear botones
    button_aplicar = tk.Button(frame, text='Apply Algorithm', command=hacer_alg)
    button_deshacer = tk.Button(frame, text='Undo last move', command=deshacer)

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
