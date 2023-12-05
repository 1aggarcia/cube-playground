from tkinter import *

from widgets.ventana import crearVentana
from constantes.enums import Cara

def main():
    ventana = crearVentana()
    ventana.mainloop()

main()

# PARA EJECUTAR PRUEBAS
# $ python -m unittest
# desde /src/

# TODO: modelos/cubo.py - escribir pruebas