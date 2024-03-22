# Ursina nos fuerza a romper estas reglas
# pylint: disable=W0401
# pylint: disable=W0622
# pylint: disable=W0614

from ursina import *

from constantes.enums import Cara
from constantes.colores import COLORES_DE_CUBO
from modelos.cubo import Cubo, generar_cubo

VECTORES_DE_CARA = {
    Cara.U: Vec3(0, 1, 0),
    Cara.D: Vec3(0, -1, 0),
    Cara.F: Vec3(0, 0, -1),
    Cara.B: Vec3(0, 0, 1),
    Cara.L: Vec3(-1, 0, 0),
    Cara.R: Vec3(1, 0, 0)
}


def ventana_ursina(dimension: int):
    aplicacion = Ursina()

    cubo_2d = generar_cubo(dimension)
    cubo_3d = _generar_cubitos(cubo_2d)

    print("---------------------")
    print(cubo_3d)
    print("---------------------")

    EditorCamera()

    return aplicacion


def _generar_cubitos(cubo: Cubo):
    dim = cubo.dimension
    desviacion = -(dim - 1) / 2

    cubitos: list[list[list[Cubito]]] = []

    for capa in range(dim):
        lista_columna = []
        for columna in range(dim):
            lista_fila = []
            for fila in range(dim):
                x = desviacion + fila
                y = desviacion + columna
                z = desviacion + capa

                if (
                    0 < capa < dim - 1
                    and 0 < columna < dim - 1
                    and 0 < fila < dim - 1
                ):
                    continue

                cubito = Cubito()
                cubito.pos(x, y, z)

                lista_fila.append(cubito)
            lista_columna.append(lista_fila)
        cubitos.append(lista_columna)

    return cubitos


def _crear_plano(raiz: Entity, cara: Cara, tono: Cara):
    plano = Entity(
        parent = raiz,
        model = 'plane',
        texture = 'white_cube',
        color = COLORES_DE_CUBO[tono],
        origin_y = -0.5
    )
    plano.look_at(VECTORES_DE_CARA[cara], 'up')

    return plano


class Cubito(Entity):
    def __init__(self):
        super().__init__()

        # valores por defecto
        self.position = Vec3(0, 0, 0)
        for cara in Cara:
            _crear_plano(self, cara, cara)

    def pos(self, x: float, y: float, z: float):
        self.position = Vec3(x, y, z)
        return self

    def input(self, key: str):
        if key == 'd':
            self.x += 1
        elif key == 'a':
            self.x -= 1
        elif key == 'w':
            self.y += 1
        elif key == 's':
            self.y -= 1
