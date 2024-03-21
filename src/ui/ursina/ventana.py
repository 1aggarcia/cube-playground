# Ursina nos fuerza a romper estas reglas
# pylint: disable=W0401
# pylint: disable=W0622
# pylint: disable=W0614

from ursina import *

from constantes.enums import Cara
from constantes.colores import COLORES_DE_CUBO
# from modelos.cubo import generar_cubo


def ventana_ursina(dimension: int):
    aplicacion = Ursina()

    # cubo = generar_cubo(dimension)
    generar_cubitos_mas_eficiente(dimension)

    EditorCamera()

    return aplicacion


def generar_cubitos_eficiente(dimension: int):
    desviacion = -(dimension - 1) / 2
    posiciones = [desviacion, -desviacion]

    # cuenta binaria para las esquinas
    for x in posiciones:
        for y in posiciones:
            for z in posiciones:
                cubito = Cubito(Cara.D)
                cubito.pos(x, y, z)

    # centros
    for z in posiciones:
        for fila in range(dimension - 2):
            for columna in range(dimension - 2):
                x = desviacion + 1 + fila
                y = desviacion + 1 + columna
                cubito = Cubito(Cara.F)
                cubito.pos(x, y, z)


def generar_cubitos_mas_eficiente(dimension: int):
    desviacion = -(dimension - 1) / 2

    for capa in range(dimension):
        for columna in range(dimension):
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

                cara_arbitraria = random.choice(list(Cara))
                cubito = Cubito(cara_arbitraria)
                cubito.pos(x, y, z)


def generar_cubitos_nxn(dimension: int):
    desviacion = -(dimension - 1) / 2

    for capa in range(dimension):
        for columna in range(dimension):
            for fila in range(dimension):
                cara_arbitraria = random.choice(list(Cara))
                cubito = Cubito(cara_arbitraria)
                cubito.pos(
                    desviacion + fila,
                    desviacion + columna,
                    desviacion + capa
                )


class Cubito(Entity):
    def __init__(self, cara: Cara):
        super().__init__()
        self.color = COLORES_DE_CUBO[cara]

        # valores por defecto
        self.position = Vec3(0, 0, 0)
        self.model = 'cube'
        self.texture = 'white_cube'

    def pos(self, x: float, y: float, z: float):
        self.position = Vec3(x, y, z)
        return self

    # def update(self):
    #     self.rotation_x += 1
    #     self.rotation_y -= 1

    def input(self, key: str):
        if key == 'd':
            self.x += 1
        elif key == 'a':
            self.x -= 1
        elif key == 'w':
            self.y += 1
        elif key == 's':
            self.y -= 1
