# import numpy as np
# import math

# from constantes.enums import Cara

# class Etiqueta:
#     '''
#     Representa una etiqueta con la cara donde pertenece y su posición, entre 1-n^2
#     '''
#     def __init__(self, cara: Cara, posicion: int):
#         self.cara = cara
#         self.posicion = posicion

#     def __str__(self):
#         return f'{self.cara.value}{self.posicion}'

#     def __eq__(self, __value: object) -> bool:
#         return (
#             isinstance(__value, Etiqueta) and
#             self.cara == __value.cara and
#             self.posicion == __value.posicion
#         )


# def etiqueta_de_texto(texto: str):
#     '''
#     Crear una Etiqueta desde una cadena de caracteres, ej 'D3'
#     * requiere que el primer carácter sea una cara
#     * requiere que los demás caracteres sean enteros
#     '''
#     # verificar que texto se puede convertir en una etiqueta
#     if len(texto) < 2:
#         raise ValueError('Etiqueta debe tener al menos 2 caracteres')
#     cara_convertida = Cara[texto[0]]
#     if cara_convertida is None:
#         raise ValueError('Etiqueta tiene que empezar con la cara')
#     posicion_convertida = int(texto[1:])

#     # crearla
#     return Etiqueta(cara_convertida, posicion_convertida)


# class Pegatina:
#     """
#     Representa una pegatina en la cara de un cubo de Rubik
#     """
#     def __init__(self, cara: Cara, profundidad: int, posicion: int):
#         self.cara = cara
#         self.profundidad = profundidad
#         self.posicion = posicion

#     def __str__(self):
#         return (
#             f'[cara: {self.cara}, '
#             f'profundidad: {self.profundidad}, '
#             f'posicion: {self.posicion}]'
#         )

#     def __eq__(self, __value: object):
#         return (
#             isinstance(__value, Pegatina) and
#             self.cara == __value.cara and
#             self.profundidad == __value.profundidad and
#             self.posicion == __value.posicion
#         )


# def crear_matriz_de_pegatinas(matriz: np.ndarray):
#     """
#     Crea un matriz nxn de Pegatinas dado un matriz nxn de Caras.
#     Cada Pegatina a [x][y] tendrá la misma cara que
#     está in matriz[x][y].

#     Su profundidad será su distancia diagonal del
#     borde, y su posición será su distancia de la esquina que
#     define su profundidad.

#     * requiere que matriz sea de dimensiones nxn, y que n >= 2
#     """
#     dimension = len(matriz)
#     if (dimension < 2):
#         raise ValueError(f'dimension < 2: {dimension}')

#     resultado = np.full((dimension, dimension), None)
#     profundidad = math.floor(dimension/2)

#     # por cara elemento en el matriz, creamos una Pegatina con la misma cara y
#     # la posición y profundidad calculada
#     for n in range(profundidad):
#         # hace más fácil las calculaciones de los índeces
#         n_inv = dimension - n - 1
#         posiciones = dimension - (2*n) - 1
#         for i in range(posiciones):
#             resultado[n, n + i] = Pegatina(
#                 matriz[n, n + 1], n, i
#             )
#             resultado[n_inv, n_inv - i] = Pegatina(
#                 matriz[n_inv, n_inv - i], n, i
#             )
#             resultado[n + i, n_inv] = Pegatina(
#                 matriz[n + i, n_inv], n, i
#             )
#             resultado[n_inv - i, n] = Pegatina(
#                 matriz[n_inv - i, n], n, i
#             )

#     # si cubo tiene dimensión impar, necesitamos agregar el centro
#     if (dimension % 2 == 1):
#         # profundidad = el centro de la matriz
#         resultado[profundidad, profundidad] = Pegatina(
#             matriz[profundidad, profundidad], profundidad, 0
#         )

#     return resultado
