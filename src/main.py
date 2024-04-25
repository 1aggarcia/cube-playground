import tkinter as tk
from tkinter import messagebox

from constantes import colores
from constantes.enums import Ventana
from ui.cubo.ventana import ventana_de_cubo
from ui.ursina.ventana import ventana_ursina


def ventana_inicial():
    ventana = tk.Tk()
    ventana.config(bg=colores.VERDE_1)
    ventana.geometry('300x200')
    ventana.eval('tk::PlaceWindow . center')

    label_dimension = tk.Label(ventana, text='Dimension:', bg=colores.VERDE_1)
    entry_dimension = tk.Entry(ventana)

    entry_dimension.insert(0, '3')

    def abrir(destino: Ventana):
        dimension = entry_dimension.get()
        if dimension.isdigit() is False:
            messagebox.showerror('Error', 'Dimension is not a number')
            return

        if int(dimension) < 2:
            messagebox.showerror('Error', f'Dimension is less than 2: {dimension}')
            return

        ventana.destroy()
        abrir_ventana(destino, int(dimension))

    button_cubo = tk.Button(ventana, text='Open new cube',
                            command=lambda: abrir(Ventana.CUBO))
    button_ursina = tk.Button(ventana, text='Ursina (Beta)',
                            command=lambda: abrir(Ventana.URSINA))

    label_dimension.grid(row=0, column=0)
    entry_dimension.grid(row=0, column=1)

    button_cubo.grid(row=1, column=0)
    #.place(relx=0.25, rely=0.66, anchor=tk.CENTER)
    button_ursina.grid(row=1, column=1)
    #.place(relx=0.75, rely=0.66, anchor=tk.CENTER)

    return ventana


def abrir_ventana(destino: Ventana, dimension: int):
    if destino == Ventana.URSINA:
        ventana_ursina(dimension).run()
    else:
        ventana_de_cubo(dimension).mainloop()


if __name__=="__main__":
    ventana_inicial().mainloop()

# PARA EJECUTAR PRUEBAS
# $ python3 -m unittest -v
# $ pylint --disable=C0114,C0115,C0116,W0511,R0913,R0801 $(git ls-files '*.py')
# desde /src/

# TODO: mejorar el algorithmo para mezclar cubos
# TODO: hacer movimientos anchos (w)
# TODO: validar cubo
# TODO: mejorar la conversión de texto -> algorithmo
