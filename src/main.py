from tkinter import *

from widgets.ventana import crearVentana

def main():
    ventana = crearVentana()
    ventana.mainloop()

if __name__=="__main__": 
    main()

# PARA EJECUTAR PRUEBAS
# $ python -m unittest
# desde /src/

# TODO: modelos/cubo.py - escribir pruebas
# TODO: actualizar la ventana más eficientemente