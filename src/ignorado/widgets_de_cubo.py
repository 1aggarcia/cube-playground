# import tkinter as tk
# from typing import Literal

# from modelos.cubo import Cubo
# from constantes import colores
# from constantes.enums import Cara
# from imagenes.impresora import imprimir_cubo

# TAMANO_DE_CARA = 160 # ancho y altura de una cara

# # métodos públicos

# def crear_label_cubo(raiz: tk.Misc, cubo: Cubo):
#     return tk.Label(raiz, text=str(cubo), bg=colores.VERDE_2, fg='#ffffff')


# def crear_frame_control(
#         raiz: tk.Misc, cubo: Cubo, callback, callback_algorithmo
#     ):
#     frame = tk.Frame(raiz, bg=colores.VERDE_2, padx=10)

#     for i, cara in enumerate(Cara):
#         button = _crear_button_control(frame, cara, 1, callback)
#         button_prima = _crear_button_control(frame, cara, -1, callback)
#         button_doble = _crear_button_control(frame, cara, 2, callback)

#         button_prima.grid(row=i, column=0)
#         button.grid(row=i, column=1)
#         button_doble.grid(row=i, column=2)

#     button_algorithmo = tk.Button(frame, text='Algorithmo', command=callback_algorithmo)
#     button_impresora = _crear_button_impresora(frame, cubo)
#     text = tk.Text(raiz, width=15, height=5)
#     text.insert(1.0, 'texto')
#     text.configure(state="disabled")

#     button_algorithmo.grid(row=7, column=4)
#     button_impresora.grid(row=8, column=4)
#     text.grid(row=1, column=1)

#     return frame


# def crear_frame_cubo(raiz: tk.Misc, cubo: Cubo):
#     frame = tk.Frame(raiz, bg=colores.VERDE_2, padx=10)

#     # crear widgets para cada cara
#     cara_u = _crear_frame_de_cara(frame, cubo, Cara.U)
#     cara_l = _crear_frame_de_cara(frame, cubo, Cara.L)
#     cara_f = _crear_frame_de_cara(frame, cubo, Cara.F)
#     cara_r = _crear_frame_de_cara(frame, cubo, Cara.R)
#     cara_b = _crear_frame_de_cara(frame, cubo, Cara.B)
#     cara_d = _crear_frame_de_cara(frame, cubo, Cara.D)

#     # posicionarlas para que se vean como un cubo plano
#     cara_u.grid(row=0, column=1)
#     cara_l.grid(row=1, column=0)
#     cara_f.grid(row=1, column=1)
#     cara_r.grid(row=1, column=2)
#     cara_b.grid(row=1, column=3)
#     cara_d.grid(row=2, column=1)

#     return frame


# def colorar_cubo(frame: tk.Frame, cubo: Cubo) -> None:
#     '''
#     Colora el frame dado con el cubo dado
#     * requiere que el frame tiene 6 niños con los nombres'u', 'd', 'l', 'r', 'f', 'b'
#     * requiere que cada nino del frame sea un Frame con nxn ninos Frame,
#         donde n = dimension del cubo
#     * modifica el frame dado, colora todos los cubitos
#     '''
#     for cara in list(Cara):
#         # chequear requisito 1
#         try:
#             cuadro = frame.nametowidget(cara.value.lower())
#             # esta función chequea requisito 2
#             # y modifica el cuadro
#             _colorar_cara(cuadro, cubo, cara)
#         except KeyError as exc:
#             raise ValueError(
#                 'REQUISITO ROTO: los ninos de frame tiene nombres incorrectos'
#             ) from exc


# # métodos privados

# def _crear_button_control(raiz: tk.Misc, cara: Cara, direccion: Literal[-1, 1, 2], callback):
#     # direccion = 1
#     texto = f'[ {cara.value} ]'
#     if direccion == -1:
#         texto = f"[ {cara.value}' ]"
#     elif direccion == 2:
#         texto = f"[ {cara.value}2 ]"
#     return tk.Button(raiz, text=texto, command=lambda: callback(cara, direccion))


# def _crear_button_impresora(raiz: tk.Misc, cubo: Cubo):
#     def imprimir():
#         imprimir_cubo(cubo)

#     return tk.Button(raiz, text='Imprimir', command=imprimir)


# def _crear_frame_de_cara(raiz: tk.Misc, cubo: Cubo, cara: Cara) -> tk.Frame:
#     '''
#     Crea un frame representando la cara dada con una matriz de nxn cubitos,
#     donde n = len(cara) indicado. Lo colora basado en el cubo dado.
#     * returns frame con el nombre de la cara en minúscula con nxn niños colorados de tamaño igual
#     '''
#     # calcular tamaño de cubitos para poder encajar todos en el frame
#     dimension = cubo.dimension
#     tamano_de_cubito = int(TAMANO_DE_CARA / dimension)

#     # crear frame central
#     frame = tk.Frame(raiz, bg='black', name=cara.value.lower(),
#                     width=TAMANO_DE_CARA, height=TAMANO_DE_CARA,
#                     borderwidth=2)

#     # llenar frame con los cubitos
#     for i in range(dimension):
#         for j in range(dimension):
#             frame_cubito = tk.Frame(
#                 frame,
#                 width=tamano_de_cubito,
#                 height=tamano_de_cubito,
#                 borderwidth=1,
#                 relief=tk.RAISED,
#             )
#             # meterlo a su posición determinada por la matriz de la que viene
#             frame_cubito.grid(row=i, column=j)

#     # colora el frame antes de devolverla
#     _colorar_cara(frame, cubo, cara)
#     return frame


# def _colorar_cara(frame: tk.Frame, cubo: Cubo, cara: Cara) -> None:
#     '''
#     Colora el frame dado con el cubo y la cara dada
#     * requiere que el frame tiene nxn ninos Frame, donde n = dimension del cubo
#     * modifica el frame dado, lo colora los cubitos
#     '''
#     dimension = cubo.dimension
#     ninos = frame.winfo_children()
#     if len(ninos) != dimension**2:
#         raise ValueError('REQUISITO ROTO: frame dado no tiene nxn ninos')

#     cuadro = cubo.get_cara(cara)

#     for i in range(dimension):
#         for j in range(dimension):
#             # ninos es 1D, las caras son 2D.
#             # El cubito [i][j] en 2D en una cara es lo mismo que
#             # el cubito [i*dimension + j] in 1D
#             cubito = ninos[i*dimension + j]
#             color = colores.COLORES_DE_CUBO[cuadro[i][j]]
#             # la modificación
#             cubito.configure(bg = color) # type: ignore
