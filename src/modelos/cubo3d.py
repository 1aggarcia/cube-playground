from modelos.cubito import Cubito
from modelos.cubo import Cubo
from constantes.enums import Cara
from constantes.colores import COLORES_DE_CUBO


class Cubo3d:
    """
    Modelo para representar un cubo de Rubik en 3D con Cubitos utilizando
    la librería Ursina.

    Debe usarse dentro de una aplicación Ursina
    """
    def __init__(self, cubitos: list[list[list[Cubito | None]]]):
        self.dimension = len(cubitos)
        self._cubitos = cubitos

    def cubitos(self):
        return self._cubitos

    def pintar(self, cubo: Cubo):
        """
        Pintar este Cubo3d con el estado actual de un Cubo de 2D.
        No modifica el argumento `cubo`.
        """
        dim = cubo.dimension
        if dim != self.dimension:
            raise ValueError(
                'La dimensión del cubo de referencia es diferente'
                + f' que la del Cubo3d: cubo.dimension = {dim},'
                + f' self.dimension = {self.dimension}'
            )

        estado = cubo.get_estado()

        for cara in Cara:
            for y, fila in enumerate(estado[cara]):
                for x, etiqueta in enumerate(fila):
                    color = COLORES_DE_CUBO[etiqueta]
                    cubito = _get_cubito(self._cubitos, x, y, cara)
                    cubito.colorar(cara, color)


def generar_cubo3d(dimension: int):
    if dimension < 2:
        raise ValueError(f'Dimension must be at least 2: {dimension}')

    desviacion = - (dimension - 1) / 2

    # crea tensor 3d lleno de `None`
    # el espacio adentro no es usado, así que se hace `None` para ahorrar recursos
    cubitos: list[list[list[Cubito | None]]] = [
        [[None for _ in range(dimension)] for _ in range(dimension)] for _ in range(dimension)
    ]

    # crear cubitos a los bordes del tensor
    for x in range(dimension):
        for y in range(dimension):
            for z in range(dimension):
                if not _es_borde(x, y, z, dimension):
                    continue

                pos_x = desviacion + x
                pos_y = desviacion + y
                pos_z = desviacion + z

                cubitos[x][y][z] = Cubito(pos_x, pos_y, pos_z)

    return Cubo3d(cubitos)


def _es_borde(x: int, y: int, z: int, dimension: int) -> bool:
    """
    Retorna `True` si las cordenadas `x`, `y`, `z` están al borde de un cubo
    NxNxN con la dimensión `dimension`
    """
    return (
        x in (0, dimension - 1)
        or y in (0, dimension - 1)
        or z in (0, dimension - 1)
    )


def _get_cubito(cubitos: list[list[list[Cubito | None]]], x: int, y: int, cara: Cara):
    """
    Retorna una referencia al cubito indicado por las coordenadas en 2D,
    y la cara especificada

    `y` y `z` deben ser en el rango de 0 - len(cubitos)
    """
    maximo = len(cubitos) - 1
    cubito = None

    if cara == Cara.D:
        cubito = cubitos[x][0][y]
    elif cara == Cara.U:
        cubito = cubitos[x][maximo][maximo - y]
    elif cara == Cara.F:
        cubito = cubitos[x][maximo - y][0]
    elif cara == Cara.B:
        cubito = cubitos[maximo - x][maximo - y][maximo]
    elif cara == Cara.L:
        cubito = cubitos[0][maximo - y][maximo - x]
    elif cara == Cara.R:
        cubito = cubitos[maximo][maximo - y][x]

    if cubito is None:
        raise ReferenceError('cubito no encontrado')

    return cubito
