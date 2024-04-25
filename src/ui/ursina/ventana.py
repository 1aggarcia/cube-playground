from ursina import EditorCamera, Ursina, Vec3

from constantes.enums import Cara
from modelos.cubo3d import generar_cubo3d

ESCALA_CAMARA = 3

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

    generar_cubo3d(dimension)
    scale = dimension / ESCALA_CAMARA
    #print(cubo.get_cubitos())

    camera = EditorCamera(ui_size = 1000)
    camera.scale_setter(Vec3(scale, scale, scale))

    return aplicacion
