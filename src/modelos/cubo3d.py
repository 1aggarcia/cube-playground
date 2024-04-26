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
    def __init__(self, cubitos: list[list[list[Cubito]]]):
        self.dimension = len(cubitos)
        self._cubitos = cubitos

    def get_cubitos(self):
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

        # la cara U
        pos_y = dim - 1
        for x, fila in enumerate(estado[Cara.U]):
            for z, col in enumerate(fila):
                pos_x = dim - x - 1
                color = COLORES_DE_CUBO[col]
                self._cubitos[pos_x][pos_y][z].colorar(Cara.U, color)

        # la cara F
        pos_x = 0
        for y, fila in enumerate(estado[Cara.F]):
            for z, col in enumerate(fila):
                pos_y = dim - y - 1
                color = COLORES_DE_CUBO[col]
                self._cubitos[pos_x][pos_y][z].colorar(Cara.F, color)

        # la cara L
            pos_z = 0
            for y, fila in enumerate(estado[Cara.L]):
                for x, col in enumerate(fila):
                    pos_y = dim - y - 1
                    pos_x = dim - x - 1
                    color = COLORES_DE_CUBO[col]
                    self._cubitos[pos_x][pos_y][pos_z].colorar(Cara.L, color)

        # ERROR: tiene la posición (0, 1, -1)
        # pero debería tener la posición (-1, 1, 0)
        # print(self._cubitos[0][2][1].position)


# TODO: reparar las posiciones
def generar_cubo3d(dimension: int):
    if dimension < 2:
        raise ValueError(f'Dimension must be at least 2: {dimension}')

    desviacion = - (dimension - 1) / 2

    cubitos: list[list[list[Cubito]]] = []

    for capa in range(dimension):
        lista_columna = []
        for columna in range(dimension):
            lista_fila = []
            for fila in range(dimension):
                x = desviacion + fila
                y = desviacion + columna
                z = desviacion + capa

                if (
                    0 < capa < dimension - 1
                    and 0 < columna < dimension - 1
                    and 0 < fila < dimension - 1
                ):
                    lista_fila.append(None)
                    continue

                cubito = Cubito()
                cubito.pos(x, y, z)

                lista_fila.append(cubito)
            lista_columna.append(lista_fila)
        cubitos.append(lista_columna)

    return Cubo3d(cubitos)
