from ursina import EditorCamera, Ursina, Vec3
from modelos.cubo3d import generar_cubo3d

ESCALA_CAMARA = 3


def ventana_ursina(dimension: int):
    aplicacion = Ursina()

    generar_cubo3d(dimension)
    #print(cubo.get_cubitos())

    escala = dimension / ESCALA_CAMARA
    camera = EditorCamera(ui_size = 1000)
    camera.scale_setter(Vec3(escala, escala, escala))

    return aplicacion
