from modelos.cubito import Cubito

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

    def hacer_nada(self):
        return


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
                    continue

                cubito = Cubito()
                cubito.pos(x, y, z)

                lista_fila.append(cubito)
            lista_columna.append(lista_fila)
        cubitos.append(lista_columna)

    return Cubo3d(cubitos)
