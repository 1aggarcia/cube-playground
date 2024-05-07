from ursina import EditorCamera, Ursina, Vec3, Entity
from modelos.cubo3d import generar_cubo3d
from modelos.cubo import generar_cubo, Cubo
from modelos.movimiento import Movimiento
from modelos.operaciones import generar_scramble

from constantes.enums import Cara
from imagenes.impresora import imprimir_cubo

ESCALA_CAMARA = 3


def iniciar_app_ursina(dimension: int):
    aplicacion = Ursina()

    cubo_3d = generar_cubo3d(dimension)

    cubo_2d = generar_cubo(dimension)
    cubo_2d.al_cambiar(lambda: cubo_3d.pintar(cubo_2d))

    escala = dimension / ESCALA_CAMARA
    camera = EditorCamera(ui_size = 1000)
    camera.scale_setter(Vec3(escala, escala, escala))

    controlador = Entity()
    controlador.input = lambda key: al_teclar(key, cubo_2d)

    aplicacion.run()


def al_teclar(key: str, cubo_2d: Cubo):
    if key == "space":
        cubo_2d.restaturar()

    elif key == "s":
        scramble = generar_scramble(cubo_2d.dimension)
        cubo_2d.ejecutar_algoritmo([str(mov) for mov in scramble])

    elif key == "i":
        imprimir_cubo(cubo_2d)

    elif key.upper() in Cara:
        mov = Movimiento(Cara[key.upper()], 1, 1, False)
        cubo_2d.mover(mov)
