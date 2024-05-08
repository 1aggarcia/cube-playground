from ursina import EditorCamera, Ursina, Vec3, Entity
from modelos.cubo3d import Cubo3d
from modelos.movimiento import Movimiento
from modelos.operaciones import generar_scramble

from constantes.enums import Cara
from imagenes.impresora import imprimir_cubo

ESCALA_CAMARA = 3


def iniciar_app_ursina(dimension: int):
    aplicacion = Ursina()

    cubo = Cubo3d(dimension)

    escala = dimension / ESCALA_CAMARA
    camera = EditorCamera(ui_size = 1000)
    camera.scale_setter(Vec3(escala, escala, escala))

    controlador = Entity()
    controlador.input = lambda key: al_teclar(key, cubo)

    aplicacion.run()


def al_teclar(key: str, cubo: Cubo3d):
    if key == "space":
        cubo.cubo_2d.restaturar()

    elif key == "s":
        scramble = generar_scramble(cubo.cubo_2d.dimension)
        cubo.cubo_2d.ejecutar_algoritmo([str(mov) for mov in scramble])

    elif key == "i":
        imprimir_cubo(cubo.cubo_2d)

    elif key.upper() in Cara:
        mov = Movimiento(Cara[key.upper()], 1, 1, False)
        cubo.cubo_2d.mover(mov)
