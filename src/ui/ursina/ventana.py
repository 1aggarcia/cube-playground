from ursina import EditorCamera, Ursina, Vec3
from modelos.cubo3d import generar_cubo3d
from modelos.cubo import generar_cubo
from modelos.operaciones import generar_scramble
from imagenes.impresora import imprimir_cubo

ESCALA_CAMARA = 3


def ventana_ursina(dimension: int):
    aplicacion = Ursina()

    cubo_2d = generar_cubo(dimension)
    scramble = generar_scramble(dimension)

    cubo_2d.ejecutar_algoritmo([str(mov) for mov in scramble])

    cubo_3d = generar_cubo3d(dimension)
    cubo_3d.pintar(cubo_2d)
    #print(cubo.get_cubitos())

    imprimir_cubo(cubo_2d)

    escala = dimension / ESCALA_CAMARA
    camera = EditorCamera(ui_size = 1000)
    camera.scale_setter(Vec3(escala, escala, escala))

    return aplicacion
