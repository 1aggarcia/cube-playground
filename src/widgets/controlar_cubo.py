import tkinter as tk
from tkinter import messagebox
from typing import Callable

import modelos.movimiento as mv
from modelos.cubo import Cubo
from constantes import colores
from imagenes.impresora import imprimir_cubo

PADDING = 10

def crear_frame_control(
        raiz: tk.Misc, cubo: Cubo, realizar_alg: Callable[[list[str]], None]
    ):
    """
    Crea y retorna el frame de control para la ventana del cubo.
    :param realizar_alg - debe ser una función que ejecute un algorítmo y
        actualice el frame apropiadamente
    """
    historial: list[str] = []

    frame = tk.Frame(raiz, bg=colores.VERDE_2)

    def hacer_alg():
        texto = text_entrada.get()
        alg = texto.split(' ')
        try:
            realizar_alg(alg)
        except (ValueError, KeyError) as e:
            messagebox.showerror('Error', f'Error: {e}')
            return

        text_entrada.delete(0, tk.END)
        historial.extend(alg)

        # ¿text_historial está vacío?
        if text_historial.compare("end-1c", "==", 1.0):
            text_historial.insert(tk.END, f'{texto}')
        else:
            text_historial.insert(tk.END, f' {texto}')

    def deshacer():
        if len(historial) == 0:
            return

        mov = mv.movimiento_de_texto(historial.pop())
        invertido = mv.invertir_movimiento(mov)
        realizar_alg([str(invertido)])
        text_historial.delete(1.0, tk.END)
        text_historial.insert(tk.END, ' '.join(historial))

    text_historial = tk.Text(frame, width=30, height=10)
    text_entrada = tk.Entry(frame, width=30)
    frame_buttons = _crear_frame_buttons(frame, cubo, hacer_alg, deshacer)

    text_historial.pack()
    text_entrada.pack()
    frame_buttons.pack()

    return frame


def _crear_frame_buttons(raiz: tk.Misc, cubo: Cubo, hacer_alg, deshacer):
    """
    Crea y retorna un frame de buttons para controlar el cubo
    """
    frame = tk.Frame(raiz, padx=PADDING, pady=PADDING)
    # crear botones
    button_aplicar = tk.Button(frame, text='Apply Algorithm', command=hacer_alg)
    button_deshacer = tk.Button(frame, text='Undo last move', command=deshacer)

    button_invertir = tk.Button(frame,
                                text='Invert Algorithm', state='disabled')
    button_reflejar = tk.Button(frame,
    text='Mirror Algorithm', state='disabled')

    button_png = tk.Button(frame, text='Export PNG',
                            command=lambda: imprimir_cubo(cubo))
    button_reset = tk.Button(frame, text='Reset Cube State', state='disabled')

    # posicionarlos
    button_aplicar.grid(row=0, column=0)
    button_deshacer.grid(row=0, column=1)

    button_invertir.grid(row=1, column=0)
    button_reflejar.grid(row=1, column=1)

    button_png.grid(row=2, column=0)
    button_reset.grid(row=2, column=1)

    return frame
