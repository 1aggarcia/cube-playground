import tkinter as tk
from tkinter import messagebox
from typing import Callable

import modelos.movimiento as mv
from modelos.cubo import Cubo
from modelos.operaciones import generar_scramble
from constantes import colores
from imagenes.impresora import imprimir_cubo

PADDING = 10

def crear_frame_control(raiz: tk.Misc, cubo: Cubo):
    """
    Crea y retorna el frame de control para la ventana del cubo.
    """
    historial: list[str] = []

    frame = tk.Frame(raiz, bg=colores.VERDE_2)

    text_historial = tk.Text(frame, width=30, height=10)
    text_entrada = tk.Entry(frame, width=30)

    text_historial.pack()
    text_entrada.pack()

    # funciones callback para actualizar la UI
    def exhibir_historial():
        text_historial.delete(1.0, tk.END)
        text_historial.insert(tk.END, ' '.join(historial))

    def hacer_alg():
        texto = text_entrada.get()
        alg = texto.split(' ')
        try:
            cubo.ejecutar_algoritmo(alg)
        except (ValueError, KeyError) as e:
            messagebox.showerror('Error', f'Error: {e}')
            return

        historial.extend(alg)
        exhibir_historial()

    def deshacer():
        if len(historial) == 0:
            return

        mov = mv.movimiento_de_texto(historial.pop())
        exhibir_historial()
        invertido = mv.invertir_movimiento(mov)
        cubo.mover(invertido)

    def mezclar():
        scramble = generar_scramble(cubo.dimension)
        scramble_str = [str(mov) for mov in scramble]

        historial.extend(scramble_str)
        exhibir_historial()
        cubo.ejecutar_algoritmo(scramble_str)

    def restatuar():
        cubo.restaturar()
        historial.clear()
        exhibir_historial()

    frame_buttons = \
        _crear_frame_buttons(frame, cubo, hacer_alg, deshacer, mezclar, restatuar)
    frame_buttons.pack()

    return frame


def _crear_frame_buttons(
        raiz: tk.Misc, cubo: Cubo, hacer_alg: Callable,
        deshacer: Callable, mezclar: Callable, restatuar: Callable
    ):
    """
    Crea y retorna un frame de buttons para controlar el cubo
    """
    frame = tk.Frame(raiz, padx=PADDING, pady=PADDING)

    # crear botones
    button_aplicar = tk.Button(frame, text='Apply Algorithm', command=hacer_alg)
    button_deshacer = tk.Button(frame, text='Undo last move', command=deshacer)

    button_invertir = tk.Button(frame,
                                text='Invert Algorithm', state='disabled')
    button_mezclar = tk.Button(frame, text='Scramble', command=mezclar)

    button_png = tk.Button(frame, text='Export PNG',
                            command=lambda: imprimir_cubo(cubo))
    button_reset = tk.Button(frame, text='Reset Cube State', command=restatuar)

    # posicionarlos
    button_aplicar.grid(row=0, column=0)
    button_deshacer.grid(row=0, column=1)

    button_invertir.grid(row=1, column=0)
    button_mezclar.grid(row=1, column=1)


    button_png.grid(row=2, column=0)
    button_reset.grid(row=2, column=1)

    return frame
