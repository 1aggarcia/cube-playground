import tkinter as tk
from tkinter import messagebox

import modelos.movimiento as mv
from modelos.cubo import Cubo
from modelos.operaciones import generar_scramble
from constantes import colores
from imagenes.impresora import imprimir_cubo

PADDING = 10


class OperadorDeCubo:
    """
    Amarrar el estado del cubo y su historial de movimientos a los widgets
    relevantes para que se pueda controlar el cubo y los widgets juntos
    """
    def __init__(self,
        cubo: Cubo, text_entrada: tk.Entry, text_historial: tk.Text
    ):
        self._cubo = cubo
        self._entrada = text_entrada
        self._text_historial = text_historial
        self._historial = []

    def aplicar_alg(self):
        texto = self._entrada.get()
        alg = texto.split(' ')
        try:
            self._cubo.ejecutar_algoritmo(alg)
        except (ValueError, KeyError) as e:
            messagebox.showerror('Error', f'Error: {e}')
            return

        self._entrada.delete(0, tk.END)
        self._historial.extend(alg)
        self._exhibir_historial()

    def deshacer(self):
        if len(self._historial) == 0:
            return

        mov = mv.movimiento_de_texto(self._historial.pop())
        self._exhibir_historial()
        invertido = mv.invertir_movimiento(mov)
        self._cubo.mover(invertido)

    def imprimir(self):
        imprimir_cubo(self._cubo)

    def mezclar(self):
        scramble = generar_scramble(self._cubo.dimension)
        scramble_str = [str(mov) for mov in scramble]

        self._historial.extend(scramble_str)
        self._exhibir_historial()
        self._cubo.ejecutar_algoritmo(scramble_str)

    def restatuar(self):
        self._cubo.restaturar()
        self._historial.clear()
        self._exhibir_historial()

    def _exhibir_historial(self):
        self._text_historial.delete(1.0, tk.END)
        self._text_historial.insert(tk.END, ' '.join(self._historial))


def crear_frame_control(raiz: tk.Misc, cubo: Cubo):
    """
    Crea y retorna el frame de control para la ventana del cubo.
    """
    frame = tk.Frame(raiz, bg=colores.VERDE_2)

    text_historial = tk.Text(frame, width=30, height=10)
    entrada = tk.Entry(frame, width=30)

    text_historial.pack()
    entrada.pack()

    operador = OperadorDeCubo(cubo, entrada, text_historial)

    frame_buttons = _crear_frame_buttons(frame, operador)
    frame_buttons.pack()

    return frame


def _crear_frame_buttons(raiz: tk.Misc, operador: OperadorDeCubo):
    """
    Crea y retorna un frame de buttons para controlar el cubo
    """
    frame = tk.Frame(raiz, padx=PADDING, pady=PADDING)

    # crear botones
    button_aplicar = tk.Button(
        frame, text='Apply Algorithm', command=operador.aplicar_alg
    )
    button_deshacer = tk.Button(
        frame, text='Undo last move', command=operador.deshacer
    )
    button_invertir = tk.Button(
        frame, text='Invert Algorithm', state='disabled'
    )
    button_mezclar = tk.Button(
        frame, text='Scramble', command=operador.mezclar
    )
    button_png = tk.Button(
        frame, text='Export PNG', command=operador.imprimir
    )
    button_reset = tk.Button(
        frame, text='Reset Cube State', command=operador.restatuar
    )

    # posicionarlos
    button_aplicar.grid(row=0, column=0)
    button_deshacer.grid(row=0, column=1)

    button_invertir.grid(row=1, column=0)
    button_mezclar.grid(row=1, column=1)


    button_png.grid(row=2, column=0)
    button_reset.grid(row=2, column=1)

    return frame
