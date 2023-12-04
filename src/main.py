from tkinter import *

from widgets.ventana import crearVentana
from constantes.enums import Cara

def main():
    vuelta()
    ventana = crearVentana()
    ventana.mainloop()

def vuelta():
    for cara in Cara:
        print(cara)

main()

# PARA EJECUTAR PRUEBAS
# $ python -m unittest
# desde /src/